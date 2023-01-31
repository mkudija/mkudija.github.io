import os
import time
import pandas as pd
import re
import shutil
import markdown2
from markdown2 import markdown_path
from distutils.dir_util import copy_tree
from pathlib import Path
import pprint


def copy_files_ifPublish(src, dst):
    """Copy directory src to directory dst if "publish" in metadata.
    """

    print('\tCopying "publish" files from a) to b): \n\t\ta) {}\n\t\tb) {}\n'.format(src, dst))

    # clear directory
    if os.path.exists(dst):
        os.system('rm -rf '+dst)
    os.makedirs(dst, exist_ok=True)

    # get all markdown files
    p = Path(src).glob('**/*.md')
    files = [x for x in p if x.is_file()]
    
    # get files to publish
    filesPublish = []
    for i, f in enumerate(files):
        if f.suffix=='.md':
            with open(f, 'r+') as f:
                line1 = f.readline()
                line2 = f.readline()
                if line2=='publish: true\n':
                    filesPublish.append(files[i])
    # pprint.pprint(filesPublish)
    
    # copy files
    for file in filesPublish:
        shutil.copyfile(file, dst+'/{}'.format(file.name))

    print('{} of {} files published ({}%)'.format(
        len(filesPublish), 
        len(files),
        round(len(filesPublish) / len(files) * 100,1)
        ))


def convert_md_to_html(src, pathSource, pathTemplate, pathOutput):
    """Converts .md (markdown) files to .html files.
    """
    print('\tConverting: {}'.format(pathSource.name))

    # metadata = get_metadata(pathSource)

    # import markdown2
    # from markdown2 import markdown_path
    with open(pathTemplate) as f:
        template = [x.strip('\n,') for x in f]
           
    template = [x.strip() for x in template] 

    title = pathSource.name.split('.')[0]
    for line in range(len(template)):
        template[line] = template[line].replace('#TITLE#', title)
            
    with open(pathSource) as f:
        md = [x.strip('') for x in f]
    
    mdString = ''.join(md)

    # add scirpts for latex and mermaid if required
    if 'latex: true' in mdString.lower():
        scriptText = '<!-- Script: Latex (Included) --> <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script> <script> MathJax = { tex: { inlineMath: [[\'$\', \'$\'], [\'\\\\(\', \'\\\\)\']]} }; </script> <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js"> </script>'
        template[template.index('<!-- Script: Latex -->')] = scriptText
    if 'mermaid: true' in mdString.lower():
        scriptText = '<!-- Script: Mermaid (Included) --> <script type="module" defer> import mermaid from \'https://cdn.jsdelivr.net/npm/mermaid@9/dist/mermaid.esm.min.mjs\'; mermaid. Initialize({ securityLevel: \'loose\', startOnLoad: true }); let observer = new MutationObserver(mutations => { for(let mutation of mutations) { mutation.target.style.visibility = "visible"; } }); document.querySelectorAll("pre.mermaid-pre div.mermaid").forEach(item => { observer.observe(item, {  attributes: true,  attributeFilter: [\'data-processed\'] }); }); </script>'
        template[template.index('<!-- Script: Mermaid -->')] = scriptText


    # style Obsidian links
    ## TODO
    ## - full support for sub-links and block links (#) (link to heading)
    ## - support for transclusions ![[]]
    ## - support for "links to this page"

    try:
        # regex help: https://regexr.com/
        # examples:   https://github.com/oleeskild/obsidian-digital-garden/blob/438f1184f16344dab177562745b4f0d72c0081ce/Publisher.ts#L160
        # linksRaw = re.findall('/\[\[(.*?)\]\]/g', mdString) # alt
        linksRaw = re.findall('(?<=\[\[).*?(?=\]\])', mdString)

        for i in linksRaw:
            linkRaw = i
            linkURL = i
            try: # for aliases (|)
                linkURL = i.split('#')[0].split('|')[0]
                i = i.split('#')[0].split('|')[1]
            except:
                i = i.split('#')[0].split('|')[0]
            linkDisplay = i
            if linkURL[0:2]=='20': # book notes are in different directory
                ## FIX: =='20' also catches daily notes, which it should not
                linkURL = linkURL.replace(' ','-') # replace spaces (not for ~ only)
                url = '../reading-notes/'+linkURL+'.html'
            elif linkURL[0]=='~': # unpublished book notes
                url = 'https://github.com/mkudija/mkudija.github.io/tree/master/reading-notes/_md/'+linkURL+'.md'
            else:
                linkURL = linkURL.replace(' ','-') # replace spaces (not for ~ only)
                url = linkURL+'.html'
            i = '<a href="'+url+'">'+linkDisplay+'</a>' # url
            linkRaw = '[['+linkRaw+']]' # only replace links, not all words that have the same title
            mdString = mdString.replace(linkRaw,i)
    except:
        print('pass')

    mdString = mdString.replace('[[','')
    mdString = mdString.replace(']]','')
    # mdString = mdString.replace('[[','<text style="background-color: whitesmoke; color: #23537d;">')
    # mdString = mdString.replace(']]','</text>')
    
    # replace "updated"
    pathSrcSource = src+str(pathSource).split('/')[-1] # use source path rather than md path to get correct updated timestamp
    updated_at = time.strftime('%Y-%m-%d-%a', time.localtime(os.path.getmtime(pathSrcSource))) # https://strftime.org/
    mdString = mdString.replace('<%+ tp.file.last_modified_date("YYYY-MM-DD") %>',updated_at) # old version, can remove eventually
    mdString = mdString.replace('<%+ tp.file.last_modified_date("YYYY-MM-DD-ddd") %>',updated_at)

    # remove metadata
    if mdString[:3]=='---':
        print('\t\tHas metadata')
        mdStringSplit = mdString.split('---')
        mdString = '---'.join(mdStringSplit[2:])


    body = markdown2.markdown(mdString, extras=['footnotes','cuddled-lists','tables','header-ids','break-on-newline', 'header-ids', 'strike', 'fenced-code-blocks', 'mermaid']) # 'target-blank-links', # extras here: https://github.com/trentm/python-markdown2/wiki/Extras
    body = [body]

    template[template.index('#BODY#')] = body

    pathOutput = pathOutput/Path((pathSource.stem+'.html').replace(' ','-'))

    with open(pathOutput, mode='wt', encoding='utf-8') as myfile:
        for lines in template:
            myfile.write(''.join(lines))
            myfile.write('\n')
    # print('\tSaved {}'.format(pathOutput))


def create_index(pathTemplate, pathOutput, fnames):
    """Create index file with links to each note.
    """

    print('\n\tGenerating index...')

    fnames.sort()
    try:
        fnames.remove('.DS_Store')
    except:
        pass
    body = ''
    for fname in fnames:
        body = body + ('\n<br><a href="{}">{}</a>'.format(fname.replace(' ','-')+'.html',fname))


    with open(pathTemplate) as f:
        template = [x.strip('\n,') for x in f]
           
    template = [x.strip() for x in template] 
            
    template[template.index('#BODY#')] = body

    with open(pathOutput, mode='wt', encoding='utf-8') as myfile:
        for lines in template:
            myfile.write(''.join(lines))
            myfile.write('\n')

    print('\nDone:\n{}\n'.format(pathOutput))


def main():
    # copy files from obsidian/ to md/
    src = '/Users/matthewkudija/Library/Mobile Documents/iCloud~md~obsidian/Documents/Obsidian/'
    dst = '../_md'
    copy_files_ifPublish(src, dst)


    # get list of paths
    p = Path('../_md').glob('**/*')
    files = [x for x in p if x.is_file()]

    # convert to html
    fnames = []
    for i in range(len(files)):
        if '~' not in str(files[i]):
            try:
                convert_md_to_html(src=src,
                                   pathSource=files[i], 
                                   pathTemplate=Path('_template.html'), 
                                   pathOutput=Path('../'))
            except:
                print('**Did not convert: {}'.format(files[i]))
            fnames.append(files[i].stem)
        else:
            print('**Did not convert: {}'.format(files[i]))


    # create index file
    create_index(pathTemplate=Path('_template.html'),
                 pathOutput=Path('../index.html'),
                 fnames=fnames)

    # TO FIX:
    # - link to files that are published
    # - render LaTeX, maybe use this? https://dev.to/siddharth2016/how-to-convert-markdown-to-html-using-python-4p1b


if __name__ == '__main__':
    main()
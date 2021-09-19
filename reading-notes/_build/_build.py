import os
import pandas as pd
# import shutil
import markdown2
from markdown2 import markdown_path
from distutils.dir_util import copy_tree
from pathlib import Path


# df = pd.read_excel('_content.xlsx',
#         converters={'shortName':str,'title':str,'author':str,'ISBN':str,'yearPublished':str,'yearRead':str})
# for row in range(df.shape[0]):
#     shortName       = df.loc[df.index[row],'shortName']
#     title           = df.loc[df.index[row],'title']
#     author          = df.loc[df.index[row],'author']
#     ISBN            = df.loc[df.index[row],'ISBN']
#     yearPublished   = df.loc[df.index[row],'yearPublished']
#     yearRead        = df.loc[df.index[row],'yearRead']
#     build(shortName, title, author, ISBN, yearPublished, yearRead)


# def copy_file(src, dst):
#     """Copy file from src to dst.
#     """

#     shutil.copyfile(src, dst)


def copy_files(src, dst):
    """Copy directory of outputs to shared drive dst.
    """

    if os.path.exists(dst):
        os.system('rm -rf '+dst)
    os.makedirs(dst, exist_ok=True)

    print('\tCopying a) to b): \n\t\ta) {}\n\t\tb) {}\n'.format(src, dst))
    copy_tree(src, dst)


def convert_md_to_html(pathSource, pathTemplate, pathOutput):
    """Converts .md (markdown) files to .html files.
    """
    print('\tConverting: {}'.format(pathSource.name))

    # metadata = get_metadata(pathSource)

    # import markdown2
    # from markdown2 import markdown_path
    with open(pathTemplate) as f:
        template = [x.strip('\n,') for x in f]
           
    template = [x.strip() for x in template] 

    # for line in range(len(template)):
    #     template[line] = template[line].replace('#TITLE#', metadata['title'])
    #     template[line] = template[line].replace('#COOKTIME#', metadata['cookTime'])
    #     template[line] = template[line].replace('#PREPTIME', metadata['prepTime'])
    #     template[line] = template[line].replace('#IMAGE#', metadata['image'])
            
    with open(pathSource) as f:
        md = [x.strip('') for x in f]
    

    # md = md[md.index('\n'):] # drop metadata from article text
    mdString = ''.join(md)


    ### style Obsidian links
    mdString = mdString.replace('[[','<text style="background-color: whitesmoke; color: #23537d;">')
    mdString = mdString.replace(']]','</text>')
    ### 


    body = markdown2.markdown(mdString, extras=['footnotes','cuddled-lists','target-blank-links','tables','templateArticleer-ids','break-on-newline', 'header-ids', 'strike']) # extras here: https://github.com/trentm/python-markdown2/wiki/Extras
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

    fnames.sort(reverse=True)
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
    src = '/Users/matthewkudija/Library/Mobile Documents/iCloud~md~obsidian/Documents/Obsidian/Reading Notes'
    dst = '../_md'
    copy_files(src, dst)

    # get list of paths
    p = Path('../_md').glob('**/*')
    files = [x for x in p if x.is_file()]

    # convert to html
    fnames = []
    for i in range(len(files)):
        if '~' not in str(files[i]):
            try:
                convert_md_to_html(pathSource=files[i], 
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
    # - render LaTeX, maybe use this? https://dev.to/siddharth2016/how-to-convert-markdown-to-html-using-python-4p1b


if __name__ == '__main__':
    main()
import numpy as np
import pandas as pd
import shutil
from pathlib import Path


def write_html(df, year):
    df = df[df['Read']==year].fillna('no author').sort_index(ascending=False) # sort_index(ascending=False) for reverse chronological order

    df['html'] = np.where(df['Author']=='no author',
        '<li><i>'+df['Title']+'</i>',
        '<li><i>'+df['Title']+'</i> by '+df['Author'])
    df['html'] = np.where((df['Notes']!='No') & (df['Notes']!='Yes'), 
        df['html']+' (<a href="'+df['Notes']+'">Notes</a>)</li>',
        df['html']+'</li>')
    df['html'] = df['html'].str.replace('by edited','edited')

    html_file = open('html/'+str(year)+'_books_html.txt', 'w')
    for row in range(df.shape[0]):
        book = str(df.loc[df.index[row],'html'])#.replace('nan','')
        html_file.write("%s\n" % book)
    html_file.close()

    numReadAll = df.shape[0]
    numRead = df[df['Type']!='Audiobook'].shape[0]

    try:
        npages  = df.loc[:,'Pages'].sum()
        print('In {} I read {} books ({} read, {}k pages).'.format(str(year), 
                                                                   str(numReadAll), 
                                                                   str(numRead),
                                                                   str(int(npages/1000))
                                                                   )
              )
    except:
        print('In {} I read {} books ({} read).'.format(str(year), 
                                                        str(numReadAll),
                                                        str(numRead)
                                                        ) 
             )

    # forecast reading (including audiobooks)
    bookForecastAll = 0
    from datetime import datetime
    if year==datetime.now().year:
        booksToDate = df.dropna(how='any',axis=0).shape[0]
        pagesToDate = df.dropna(how='any',axis=0).loc[:,'Pages'].sum()
        dayOfYear = datetime.now().timetuple().tm_yday
        bookForecastAll = booksToDate / dayOfYear * 365
        pageForecastAll = pagesToDate / dayOfYear * 365

    # forecast reading (less audiobooks)
    df = df[df['Type']!='Audiobook']
    bookForecastRead = 0
    from datetime import datetime
    if year==datetime.now().year:
        booksToDate = df.dropna(how='any',axis=0).shape[0]
        pagesToDate = df.dropna(how='any',axis=0).loc[:,'Pages'].sum()
        dayOfYear = datetime.now().timetuple().tm_yday
        bookForecastRead = booksToDate / dayOfYear * 365
        pageForecastRead = pagesToDate / dayOfYear * 365
        print('...on track to read {} ({}) books ({}k ({}k) pages) in {}'.format(int(bookForecastAll),
                                                                                 int(bookForecastRead),
                                                                                 int(pageForecastAll/1000),
                                                                                 int(pageForecastRead/1000),
                                                                                 year)
              )

    return bookForecastAll, bookForecastRead


def plot_books(df, years, bookForecastAll, bookForecastRead):
    import matplotlib.pyplot as plt

    print('\nPlotting...')

    # don't plot 2005 and before
    df = df[df['Read']!=2005]
    df2 = df[df['Type']!='Audiobook']
    years = years[1:]

    number = []
    for year in years:
        df_count = df[df['Read']==year]
        number.append(df_count.shape[0])

    numberRead = []
    for year in years:
        df_count = df2[df2['Read']==year]
        numberRead.append(df_count.shape[0])

    fig, ax = plt.subplots()
    ax.axis('off')
    plt.bar(years[-1], bookForecastAll, color='#ffffff', edgecolor='#909090')
    plt.bar(years, number, color='#3377b3')
    plt.bar(years, numberRead, color='#2a6394')
    for item in range(0,len(years)):
        plt.text(years[item], -8, str(years[item]),ha='center',color='#63666a',fontname='Gill Sans MT',fontsize=14)
    fig.set_size_inches(12, 4)
    fig.savefig(str(GitHubPath)+'/mkudija.github.io/images/book_plot.png',
                bbox_inches='tight',
                transparent=True)


def copy_file(src, dst):
    """Copy file from src to dst.
    """
    src = str(src)
    dst = str(dst)
    shutil.copy(src, dst)


def insert_text_in_file(originalPath, addPath, insertionPoint):
    """Inserts text from add into original at insertionPoint
    """
    # read original 
    f = open(originalPath, "r")
    contents = f.readlines()
    f.close()

    # read add 
    f = open(addPath, "r")
    add = f.readlines()
    f.close()

    # get index of insertionPoint
    i=0
    for line in contents:
        if insertionPoint in line:
            index = i
        i+=1

    # add text
    contents[index:index] = add

    # write original with addition
    f = open(originalPath, "w")
    contents = "".join(contents)
    f.write(contents)
    f.close()


def construct_index(years, pathOutput):
    """Copies reading.html to pathOutput, and constructs page using years.
    """

    # copy index from template
    copy_file('reading-template.html', pathOutput)

    for year in years:
        addPath = 'html/'+str(year)+'_books_html.txt'
        insertionPoint = '<!-- ADD '+str(year)+' READING -->'
        insert_text_in_file(pathOutput, addPath, insertionPoint)


if __name__ == "__main__":
    homePath = Path.cwd().home()
    for parent in Path.cwd().parents:
        if str(parent)[-6:]=='GitHub':
            GitHubPath = parent

    df = (pd.read_excel(GitHubPath/'mkudija.github.io/reading/reading.xlsx',sheet_name='Books')
        .dropna(axis=0, thresh=3)
        )

    years = df['Read'].unique()

    for year in years:
        bookForecastAll, bookForecastRead = write_html(df, year)
    
    plot_books(df, years, bookForecastAll, bookForecastRead)

    print('\nBuilding reading.html...')
    construct_index(years, pathOutput='../reading.html')

    print('\nDone.')
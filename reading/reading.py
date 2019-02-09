import numpy as np
import pandas as pd
import shutil
from pathlib import Path


def write_html(df, year):
    df = df[df['Read']==year].fillna('no author')
    df['html'] = np.where(df['Author']=='no author',
        '<li><i>'+df['Title']+'</i></li>',
        '<li><i>'+df['Title']+'</i> by '+df['Author']+'</li>')
    df['html'] = df['html'].str.replace('by edited','edited')

    html_file = open('html/'+str(year)+'_books_html.txt', 'w')
    for row in range(df.shape[0]):
        book = str(df.loc[df.index[row],'html'])#.replace('nan','')
        html_file.write("%s\n" % book)
    html_file.close()

    print('In {} I read {} books.'.format(str(year),str(df.shape[0])))

    # forecast reading
    bookForecast = 0
    from datetime import datetime
    if year==datetime.now().year:
        booksToDate = df.dropna(how='any',axis=0).shape[0]
        dayOfYear = datetime.now().timetuple().tm_yday
        bookForecast = booksToDate / dayOfYear * 365
        print('...on track to read {} books in {}'.format(int(bookForecast), year))
    return bookForecast
 

def plot_books(df, years, bookForecast):
    import matplotlib.pyplot as plt

    print('\nPlotting...')

    # don't plot 2005 and before
    df = df[df['Read']!=2005]
    years = years[1:]

    number = []
    for year in years:
        df_count = df[df['Read']==year]
        number.append(df_count.shape[0])

    fig, ax = plt.subplots()
    ax.axis('off')
    plt.bar(years[-1], bookForecast, color='#ffffff', edgecolor='#909090')
    plt.bar(years, number, color='#3377b3')
    for item in range(0,len(years)):
        #plt.text(years[item], number[item]+3, str(number[item]),ha='center',color='#63666a',fontname='Gill Sans MT',fontsize=14)
        plt.text(years[item], -8, str(years[item]),ha='center',color='#63666a',fontname='Gill Sans MT',fontsize=14)
    fig.set_size_inches(12, 4)
    fig.savefig(str(GitHubPath)+'/mkudija.github.io/images/book_plot.png'
                , bbox_inches='tight'
                , transparent=True)


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
    copy_file('reading.html', pathOutput)

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
        bookForecast = write_html(df, year)
    
    plot_books(df, years, bookForecast)

    print('\nBuilding reading.html...')
    construct_index(years, pathOutput='../reading.html')

    print('\nDone.')
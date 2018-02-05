import numpy as np
import pandas as pd
from pathlib import Path


def write_html(df, year):
    df = df[df['Read']==year]
    df['html'] = '<li><i>'+df['Title']+'</i> '+df['Author']+'</li>'

    html_file = open('html/'+str(year)+'_books_html.txt', 'w')
    for row in range(df.shape[0]):
        book = df.loc[df.index[row],'html']
        html_file.write("%s\n" % book)
    html_file.close()

    print('In {} I read {} books.'.format(str(year),str(df.shape[0])))


def plot_books(df, years):
    import matplotlib.pyplot as plt
    number = []
    for year in years:
        df_count = df[df['Read']==year]
        number.append(df_count.shape[0])

    fig, ax = plt.subplots()
    ax.axis('off')
    plt.bar(years, number, color='#3377b3')
    for item in range(0,len(years)):
        #plt.text(years[item], number[item]+3, str(number[item]),ha='center',color='#63666a',fontname='Gill Sans MT',fontsize=14)
        plt.text(years[item], -6, str(years[item]),ha='center',color='#63666a',fontname='Gill Sans MT',fontsize=14)
    fig.set_size_inches(12, 4)
    fig.savefig(str(GitHubPath)+'/mkudija.github.io/images/book_plot.png', bbox_inches='tight')


if __name__ == "__main__":
    homePath = Path.cwd().home()
    for parent in Path.cwd().parents:
        if str(parent)[-6:]=='GitHub':
            GitHubPath = parent

    df = pd.read_excel(GitHubPath/'mkudija.github.io/reading/reading.xlsx',sheet_name='Books')
    years = df['Read'].unique()

    for year in years:
        write_html(df, year)
    
    plot_books(df, years)

    print('Done.')
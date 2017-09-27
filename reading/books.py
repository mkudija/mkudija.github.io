years = [2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017]

def books_by_year(year): 
    # import books
    filename = year+'_Books.md'
    with open(filename) as f:
        books = f.readlines()

    # reformat for HTML
    books = [x.strip('\n') for x in books] 
    books_html = [x.replace('- *','<li><i>').replace('* ','</i> ').replace('*','</i> ')+'</li>' for x in books]

    # save HTML formatting
    html_file = open('html/'+year+'_books_html.txt', 'w')
    for book in books_html:
        html_file.write("%s\n" % book)
    html_file.close()

    print('In '+year+' I read '+str(len(books))+' books.')
    return len(books)

number = []
for year in years:
    x = books_by_year(str(year))
    number.append(x)



import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.axis('off')
plt.bar(years, number, color='#3377b3')
for item in range(0,len(years)):
    #plt.text(years[item], number[item]+3, str(number[item]),ha='center',color='#63666a',fontname='Gill Sans MT',fontsize=14)
    plt.text(years[item], -6, str(years[item]),ha='center',color='#63666a',fontname='Gill Sans MT',fontsize=14)
fig.set_size_inches(12, 4)
fig.savefig('/Users/mkudija/Documents/Matthew/GitHub/mkudija.github.io/images/book_plot.png', bbox_inches='tight')

print('Done.')
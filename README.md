# mkudija.github.io
> [Matthew Kudija Personal Website](http://matthewkudija.com/)

## License
The basic theme is an adapted version of [Editorial by HTML5 UP](https://html5up.net/editorial).

```
Editorial by HTML5 UP
html5up.net | @ajlkn
Free for personal and commercial use under the CCA 3.0 license (html5up.net/license)
```

Content © 2005-2017 Matthew Kudija

# How It's Made

## 1. Set Up GitHub Pages

## 2. Download HTML5 UP Theme

## 3. Set Up Extras
- 404.html
- CNAME
- favicon.ico
- robots.txt

## 4. Enable Bigfoot Footnotes

## 5. Update Books
- add cover image to [`images/books/`](images/books/)
- add data in `books/md/_content.xlsx`
- run `books/md/_build.py`

### Manual .MD to .HTML
Run [`markdown2.py`](/book-reviews/md/markdown2.py) to convert Markdown to HTML. See [here](https://github.com/trentm/python-markdown2) for more information about markdown2 from @trentm.

```
python markdown2.py -x footnotes,smarty-pants,cuddled-lists FNAME.md > FNAME.html
```

## 6. Update Reading
Run [`books.py`](/reading/books.py) to covert book list from Markdown to HTML. This also generates a plot.

```
python books.py
```


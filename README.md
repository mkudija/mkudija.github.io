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
### 404.html
### CNAME
### favicon.ico
### robots.txt
### Google Analytics
Set up [Google Analytics](https://analytics.google.com/analytics/web/) to get your unique tracking ID (mine is `UA-72240498-1`) and then copy the required code in to your HTML pages:

> This is the Global Site Tag (gtag.js) tracking code for this property. Copy and paste this code as the first item into the `<HEAD>` of every webpage you want to track. If you already have a Global Site Tag on your page, simply add the **config** line from the snippet below to your existing Global Site Tag.

```html
<!-- Global Site Tag (gtag.js) - Google Analytics -->
		<script async src="https://www.googletagmanager.com/gtag/js?id=UA-72240498-1"></script>
		<script>
			window.dataLayer = window.dataLayer || [];
			function gtag(){dataLayer.push(arguments);}
			gtag('js', new Date());
			gtag('config', 'UA-72240498-1');
		</script>
```


## 4. Enable Bigfoot Footnotes
See [this commit](https://github.com/mkudija/mkudija.github.io/commit/8f6ed3f882466ee92a2aa00a8afec854b9b390ec)
- to change button appearance, customize class "bigfoot-footnote__button" properties in [`bigfoot-default.css`](assets/css/bigfoot-default.css)
- to change popup appearance, customize class "bigfoot-footnote__content" properties in [`bigfoot-default.css`](assets/css/bigfoot-default.css)

## 5. Update Books
1. write book review in markdown
	* See [easybib](http://www.easybib.com/guides/citation-guides/chicago-turabian/footnotes/) exmple for footnote formatting: `Henry James, The Ambassadors (Rockville: Serenity, 2009), 34-40.` Footnotes in Markdown use this format:
```
"Blah blah blah."[^id] More words and more words.[^id2] Finally, let's add more words

[^id]: Footnote text for id1 goes here...
[^id2]: Footnote text for id2 goes here...
```

	* 
2. add cover image to [`images/books/`](images/books/)
3. add data in `books/md/_content.xlsx`
4. run `books/md/_build.py`
5. commit changes (including newly created html file)

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


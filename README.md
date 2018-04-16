# mkudija.github.io
> [Matthew Kudija Personal Website](http://matthewkudija.com/)

## License
The basic theme is an adapted version of [Editorial by HTML5 UP](https://html5up.net/editorial).

```
Editorial by HTML5 UP
html5up.net | @ajlkn
Free for personal and commercial use under the CCA 3.0 license (html5up.net/license)
```

Content © 2005-2018 Matthew Kudija

# How It's Made

## 1. Set Up GitHub Pages

## 2. Download HTML5 UP Theme

## 3. Set Up Extras
### 404.html
### CNAME
### favicon.ico
### robots.txt
I added a robots.txt but removed it after seeing that it messed up Google search results
### sitemap.xml
I added a sitemap to aid in searching (and perhaps eventually get sitelinks on the search result) from [xml-sitemaps.com](https://www.xml-sitemaps.com)
### meta tag
I updated the meta tag to improve search results.
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

2. add cover image to [`images/books/`](images/books/)
3. add data in [`books/md/_content.xlsx`](books/md/_content.xlsx)
4. run [`books/md/_build.py`](books/md/_build.py) which creates an HTML file for each MD file defined in `_content.xlsx`\*
5. commit changes (including newly created html file)

\*Alternatively, individually convert from MD to HTML in the commany line by running [`markdown2.py`](/book-reviews/md/markdown2.py) (See [here](https://github.com/trentm/python-markdown2) for more information about markdown2 from @trentm):

```
python markdown2.py -x footnotes,smarty-pants,cuddled-lists,target-blank-links FNAME.md > FNAME.html
```

## 6. Update Reading
Run [`reading.py`](/reading/reading.py) to covert book list from Markdown to HTML. This also generates a plot.

```
python reading.py
```

<h1 id="examples">Example Websites</h1>

- [Knight Lab](https://knightlab.northwestern.edu/), including [Juxtapose for comparing images](https://juxtapose.knightlab.com/) and a [cool book timeline](https://cdn.knightlab.com/libs/timeline3/latest/embed/index.html?source=1wNbJv1Zf4Oichj3-dEQXE_lXVCwuYQjaoyU1gGQQqk4&font=Default&lang=en&start_at_end=true&initial_zoom=2&height=650)
- [Chris Moffitt](http://pbpython.com/)
- [Jake VanderPlas](http://jakevdp.github.io/)
- [Tim Hopper](https://tdhopper.com/)
- [Kieran Healy](https://kieranhealy.org/resources/)
- [Michael Zalewski](http://lcamtuf.coredump.cx/table/)
- [David Robinson](http://varianceexplained.org/r/start-blog/)
- [Gavin Rehkemper](https://gavinr.com/about-gavin-rehkemper/)
- [Daniel Rodriguez](danielfrg.com)
- [Matthew Henderson](http://www.matthen.com/)
- [Joe Hanson](https://www.itsokaytobesmart.com/)
- [Ian Schon](http://ianschon.com/)
- [Brett Victor](http://worrydream.com/)
- [Chris Olah](http://colah.github.io/)
- [John Cook](https://www.johndcook.com/blog/)
- [Jonathan McGlone](http://jmcglone.com/about/)
- [Chris Albon](https://chrisalbon.com/)
- [Jeff Atwood](https://blog.codinghorror.com/about-me/)
- [Duncan Lock](http://duncanlock.net/pages/duncan-locks-resume.html)
- [Matti Vuorre](https://vuorre.netlify.com/)
- [Cody McLain](https://www.codymclain.com/photography/)
- [Justin Ellis](https://jellis18.github.io/)
- [Jeroen Boeye](https://www.jeroenboeye.com/about/)
- [Michael Herman](http://mherman.org/about)
- [Nipun Batra](https://nipunbatra.github.io/blog/2017/Jupyter-powered-blog.html)











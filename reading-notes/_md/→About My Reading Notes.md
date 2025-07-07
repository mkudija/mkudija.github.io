
# About My Reading Notes

Welcome to my reading notes page. 

These notes serve as a map for myself to navigate some ideas and information I have encountered in my intellectual adventures. A note is a way to record my engagement with a text, and it naturally grows over time and helps me retain more of what I read.[^Bayard] I enjoy revisiting ideas and comparing them across works—taking notes in [Obsidian](https://obsidian.md/) is lends itself to this linked note-taking. Taking notes, especially summarizing or reflecting on a work, is an opportunity to think more deeply about what I read.

[^Bayard]: cf. Pierre Bayard,  *[[2021-06-01-How to Talk About Books You Haven't Read|How to Talk About Books You Haven't Read]]* (New York: Bloomsbury, 2007)

Why bother sharing these notes online? My primary audience is my future self and it's handy to be able to reference these notes from anywhere with a web browser. It's also convenient to share the URL of a note with someone. Finally, if you stumble across these and find them useful that's an added fruit of my studies![^fruit] [Here](https://github.com/mkudija/mkudija.github.io/tree/master/reading#others-with-book-lists) are some others who share their notes and reading lists on the internet.

[^fruit]: Study ought to be fruitful rather than sterile, as a KJV translator's note on Augustine "highlights Bois's limitations: he gives nothing new. It is essentially the kind of note a student makes for himself: the extended time and daily labour, Christmas day included, that he devoted to Augustine do indeed show habitual, tenacious but essentially sterile study." (*[[2025-07-06-The King James Bible-A Short History from Tyndale to Today|The King James Bible-A Short History from Tyndale to Today]]*, 76)

These notes range from a few quotes I wanted to save (*[Walden](https://matthewkudija.com/reading-notes/2016-01-08-Walden.html)* and *[Walking](https://matthewkudija.com/reading-notes/2019-12-30-Walking.html)*) to detailed notes and reflections (*[After Virtue](https://matthewkudija.com/reading-notes/2020-11-18-After-Virtue.html)* and *[Witness to Hope](https://matthewkudija.com/reading-notes/2021-07-20-Witness-to-Hope.html)*). In general, more recent notes are more detailed as I have sought to slow down and engage more deeply with what I read.

I practice a version of [[The Fractal-Summary Method]] of reading, where the unit of text summarized is a function of the text itself and the amount of time I invest in it. Ideally, I summarize at least at the chapter level. 

My process for producing these notes is approximately as follows:

Before reading (often long before I even own a book) I create a note in Obsidian. I use the [obsidian-book-search-plugin](https://github.com/anpigon/obsidian-book-search-plugin) to populate metadata about the book. I also use this template for the remainder of the note: [[~Templater-Book Note]]

For **physical books** I own I will underline and write in the margins as I read. My annotation convention includes:
- underline key passages (with a star to emphasize the most important)
- brackets around less important or longer sections
- numbers for concepts that can be represented as a list
- circles around key names or concepts at the beginning of the section that discusses them
- rectangles around words I don't know
- arrows pointing at books mentioned I want to look into
- notes in the margins or at the bottom of the page for paragraph- or page-level summaries
- notes on the last page of the chapter with the chapter-level summary

After reading, or ideally after reading a section, I transcribe these notes to Obsidian, usually rather less than I originally annotated but with page numbers so I can come back to that place in the text. Finally I add my personal summary or reflection to synthesize my encounter with the text. Physical books I own represent about 50–60% my reading historically, but recently have become closer to 80-90% as I focus on engaging with the text more which really requires a physical copy that I can mark up.

For **physical books I do not own**—borrowed from the library or a friend—I take notes while reading in Obsidian or with a pen on a piece of paper if I want to be fully offline. Physical books I do not own represent about 10% my reading.

For **audiobooks** from my library played through the Libby app, I make bookmarks as I go along. When the book is finished, I use a simple Google Sheet to interpolate the percent complete vs page number so I can revisit the bookmarks in the physical text and take notes as appropriate. Audiobooks used to be a significant fraction of my "reading" (30–40%), but have since diminished as I both engage deeper with reading that requires a physical text and preserve "audio time" for select podcasts or listening to [[The Bible]].

For **electronic books** on Kindle or in a PDF I highlight while reading and then bring these notes into a markdown file in Obsidian as above. I tend to massively over-highlight, especially on Kindle, which is why I always prefer reading a physical copy. The effort it takes to type a thought or transcribe a passage is a helpful filter. Electronic books represent less than 5% of my reading, which the exception of magisterial documents which I prefer to read directly from the Vatican website.

I mentioned my [template file](https://raw.githubusercontent.com/mkudija/mkudija.github.io/master/reading-notes/_md/~Templater-Book%20Note.md) which has a few standard elements:
- metadata: title, author, publisher, year published, number of pages, image
- before "notes" I will add a personal summary or reflection for books I engage with the most
- the table of contents is populated using a Sublime Text plugin for longer notes (and enclosed in and HTML `<details>` tag to collapse it)
- chapter dividers, with a summary section for each
- a section for bibliography and new words to track the most important or interesting books referenced as well as the definition of any new words I come across in the text (as of 2022-06 my bibliography consists of a simple query like `[[bib]] file:(<%tp.file.title%>)` which allows me to note referenced works sprinkled throughout the note and see a consolidated list in this section)

Since moving my reading note markdown files to Obsidian in 2020-2021 I have been able to engage with them much more deeply than before by linking related ideas across books. I have also revisited notes more frequently and added to them as I read more related topics. 

To publish my notes from Obsidian to my website, [this script](https://github.com/mkudija/mkudija.github.io/blob/master/reading-notes/_build/_build.py) grabs each markdown file, converts it HTML, inserts the HTML into a template, and saves a copy of both the markdown and HTML to Github as a backup and to publish. 

---
Created: [[2021-09-02-Thu]]
Updated: `=dateformat(this.file.mtime, "yyyy-MM-dd-ccc")`

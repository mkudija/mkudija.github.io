
# About My Reading Notes

Welcome to my reading notes page. 

These notes serve as a map for myself to navigate some ideas and information I have encountered in my intellectual adventures. A note is a lightweight way to revisit what I have previously read and what I am therefore unfortunately and continually forgetting[^Bayard]. I enjoy revisiting ideas and  comparing them across works—[Obsidian](https://obsidian.md/) is particularly well suited for this and now the home of all my reading notes. Taking notes, especially summarizing or reflecting on a work, is an opportunity to think more deeply about what I read.

[^Bayard]: cf. Pierre Bayard, *[How to Talk About Books You Haven't Read](https://matthewkudija.com/reading-notes/2021-06-01-How-to-Talk-About-Books-You-Haven't-Read.html)* *[[[2021-06-01-How to Talk About Books You Haven't Read]]]* (New York: Bloomsbury, 2007)

Why bother sharing these notes online? My primary audience is my future self and it's handy to be able to reference these notes from anywhere with a web browser. It's also convenient to share a note with a friend with a URL. Finally, if you stumble across these and find them useful that's great! [Here](https://github.com/mkudija/mkudija.github.io/tree/master/reading#others-with-book-lists) are some others who share their notes and reading lists on the internet.

These notes range from a few quotes I wanted to save (*[Walden](https://matthewkudija.com/reading-notes/2016-01-08-Walden.html)* and *[Walking](https://matthewkudija.com/reading-notes/2019-12-30-Walking.html)*) to detailed notes and reflections (*[After Virtue](https://matthewkudija.com/reading-notes/2020-11-18-After-Virtue.html)* and *[Witness to Hope](https://matthewkudija.com/reading-notes/2021-07-20-Witness-to-Hope.html)*). In general, more recent notes are more detailed.

My process for producing these notes is approximately as follows:

For **physical books** I own I will underline and write in the margins as I read. My annotation convention includes:
- underline key passages (with a star to emphasize the most important)
- brackets around less important or longer sections
- numbers for concepts that can be represented as a list
- circles around key names or concepts at the beginning of the section that discusses them
- rectangles around words I don't know
- arrows pointing at books mentioned I want to look into
- notes in the margins with my thoughts or referencing related texts

At the end of each chapter I write a short summary of the key ideas of that chapter. When I finish the book I make a new note file in markdown in Obsidian from a template ([[~Templater-Book Note]]) and transcribe edited chapter summaries. I then transcribe quotes I underlined or notes about the ideas presented, usually rather less than I originally annotated but with page numbers so I can come back to that place in the text. Finally I add my personal summary or reflection to synthesize my encounter with the text. Physical books I own represent about 50–60% my reading.

For **audiobooks** from my library played through the Overdrive app, I keep notes in the [Reading List](https://apps.apple.com/us/app/reading-list-book-tracker/id1217139955) app on my phone while I listen. These notes are necessarily sparse but I will occasionally transcribe an important passage exactly. I request the physical copy of the book from the library as well so I can look up passages and read relevant sections in more detail. After listening to the book, I create a markdown book note and clean up or add to the notes taken while listening. About 30–40% of the books I "read" are Audiobooks.

For **physical books I do not own**—borrowed from the library or a friend—I take notes while reading in the Reading List app or with a pen on a piece of paper if I want a fully disconnected reading experience. When complete, I move these notes into a markdown file in Obsidian as above. Physical books I do not own represent about 10% my reading.

For **electronic books** on Kindle or in a PDF I highlight while reading and then bring these notes into a markdown file in Obsidian as above. I tend to massively over-highlight, especially on Kindle, which is why I always prefer reading a physical copy. The effort it takes to type a thought or transcribe a passage is a helpful filter. Electronic books represent less than 5% of my reading.

I mentioned my [template file](https://raw.githubusercontent.com/mkudija/mkudija.github.io/master/reading-notes/_md/~Templater-Book%20Note.md) which has a few standard elements:
- metadata: title, author, publisher, year published, number of pages, image
- before "notes" I will add a personal summary or reflection for books I engage with the most
- the tables of contents is populated using a Sublime Text plugin for longer notes (and enclosed in and HTML `<details>` tag to collapse it)
- chapter dividers, with a summary section for each
- a section for bibliography and new words to track the most important or interesting books referenced as well as the definition of any new words I come across in the text

Since moving my reading note markdown files to Obsidian I have started engaging with them much more deeply than before by linking related ideas across books. I have also revisited notes more frequently and added to them as I read more related topics. This is still new to me and I'm excited to see how these connections organically emerge over time. 

To publish my notes from Obsidian to my website, [this script](https://github.com/mkudija/mkudija.github.io/blob/master/reading-notes/_build/_build.py) grabs each markdown file, converts it HTML, inserts the HTML in a template, and saves a copy of both the markdown and HTML to Github as a backup and to publish. 


**Resources**

- [The Fractal-Summary Method: How to Read Great Books](https://johnathanbi.com/essays/fractal-summary-method)

---
Created: [[2021-09-02-Thu]]
Updated: <%+ tp.file.last_modified_date("YYYY-MM-DD-ddd") %>

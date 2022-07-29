---
publish: true
---
*[[Personal Knowledge Management]]*

# Obsidian
>[Obsidian](https://obsidian.md/) is "A second brain[^sb], for you, forever. Obsidian is a powerful **knowledge base** on top of a **local folder** of plain text Markdown files."

[^sb]: cf. *[[2022-07-15-Building A Second Brain|Building a Second Brain]]* by [[Tiago Forte]]

I started using Obsidian in early 2021—my first daily note is [[2021-02-16-Tue]].

## Hotkeys
- `⌘+Enter` - check off list
- `⌘+⇧+Enter` = `Command+Shift+Enter` = Tasks: Create or Edit Task
- `⌥+⌘+Enter` = `Option+Command+Enter` = Open Link in new pane
- `⌥+Enter` = `Option+Enter` = Open Link in existing pane pane
- `⌘⇧F` - search all notes ([search docs](https://help.obsidian.md/Plugins/Search))
- `⇧⌃H` - toggle left sidebar
- `⇧⌃L` - toggle right sidebar
- `⌘ + +/-` - zoom in/out
- `⌥⌘+I` = `Option+Command+I` = Open inspector (for CSS, etc.)
- `F2` - select file title
- [Santi Younger's hotkeys](https://santiyounger.com/obsidian-shortcuts/)

## Syntax
- `[[Link]]` to link to a note
- `![[Link]]` to fully transclude that note!
- `[[Link]]` + `#` to reference a section
- `[[Link]]` + `^` to reference a block
- `[[^^...]]` to reference blocks across the vault (regardless of note)

## Plugins
*These are some of the plugins I use, ordered approximately by frequency or importance of use.*

### [obsidian-tasks](https://github.com/schemar/obsidian-tasks#installation)
- I use this paired with Espanso shortcuts for `;tod` and `;tom` to generate the completion time `📅 YYYY-MM-DD`
- [priority](https://obsidian-tasks-group.github.io/obsidian-tasks/getting-started/priority/)
	-  ⏫ for high priority
	-  🔼 for medium priority
	-  🔽 for low priority

### [Templater](https://github.com/SilentVoid13/Templater)
- [[Templater-Ben Newton Daily Note Template]]
	- Ben Newton's [daily note template](https://gist.githubusercontent.com/bennewton999/62b4a034445a24532591bc4c55a52cf5/raw/83cb9636f00f724042905774f5bbb2def5331ee8/dailyNoteTemplate.txt) ([email 2021-08-17](https://mail.google.com/mail/u/0/?pli=1#inbox/KtbxLwghgcJtBxGpfJmfkQBDQmfMfcMmgq))
- [[Templater-Created & Updated]]
- [[Templater-Person-Detailed]]
- [[Templater-Aliases]]
- [Docs](https://silentvoid13.github.io/Templater/)

### [obsidian-todoist-plugin](https://github.com/jamiebrynes7/obsidian-todoist-plugin)
- Paired with the Todoist browser plugin, this forms part of my capture from email to Obsidian: emails are batch processed and tasks and consume later are moved to Obsidian with the plugin

### [obsidian-auto-link-title](https://github.com/zolrath/obsidian-auto-link-title)
- Generates markdown links within Obsidian after pasting a URL
- Mostly replaces the "copy as markdown" browser plugin (though this is still needed for work links that require authentication)
- From [Practically Paperless with Obsidian, Episode 17: Six Ways I Use Note Links – Jamie Todd Rubin](https://jamierubin.net/2022/02/08/practically-paperless-with-obsidian-episode-17-six-ways-i-use-note-links/)

### [obsidian-book-search-plugin](https://github.com/anpigon/obsidian-book-search-plugin)
- Starting [[2022-07-15-Fri]] this is how I populate metadata for my [[→About My Reading Notes|Reading Notes]]

### [omnisearch](https://github.com/scambier/obsidian-omnisearch)

### [note-refactor-obsidian](https://github.com/lynchjames/note-refactor-obsidian)

### [obsidian-excel-to-markdown-table](https://github.com/ganesshkumar/obsidian-excel-to-markdown-table)

### [obsidian-dataview](https://github.com/blacksmithgu/obsidian-dataview)
- Dataview query on each person's page for next meeting (from [here](https://medium.com/@benenewton/how-i-use-obsidian-to-track-topics-for-my-one-on-one-meetings-35b1907526ff))

```dataviewjs

dv.taskList(dv.pages().file.tasks.where(t => !t.completed && t.text.includes("[[Dana]]")))
```

Last updated:
```dataview
table file.mday
where file.name = "Sacred Artwork"
```


### Jupyter
*allows you to run python in Obsidian*

- Set path in settings to: `/opt/anaconda3/bin/python`

```jupyter
x = 1+2
print('x = {}'.format(x))
```

```jupyter
import numpy as np
from matplotlib import pyplot as plt
x = np.linspace(0,1)
y = np.exp(x) * np.sin(40 * np.pi * x)
plt.plot(x, y)
pass
```

```jupyter
import pandas as pd
df=pd.read_html('https://en.wikipedia.org/wiki/List_of_Catholic_saints')
print(df[2].head())
```

### [obsidian-various-complements-plugin](https://github.com/tadashi-aikawa/obsidian-various-complements-plugin) (auto-complete)

### Plugins to try out?
- [obsidian-query-language](https://github.com/jplattel/obsidian-query-language), can control order of search ([link](https://canburaks.gitbook.io/webmeister-s-wiki/code/apps-api/obsidian/obsidian-search))
- [Fleeting Notes | A scratchpad for connected notes](https://fleetingnotes.app/)
- [How to Create a BookShelf To Track Books in Obsidian | by Prakash Joshi Pax | May, 2022 | Medium](https://beingpax.medium.com/how-to-create-a-bookshelf-to-track-books-in-obsidian-f5130555be44)
- 


## Obsidian Publish
[Obsidian Publish](https://obsidian.md/publish) is a paid service to publish part of your vault online. I use my own pair of scripts for [notes](https://github.com/mkudija/mkudija.github.io/blob/master/notes/_build/_build.py) and [reading notes](https://github.com/mkudija/mkudija.github.io/blob/master/reading-notes/_build/_build.py) to publish from my vault with limited functionality, and I am tracking [[Obsidian Publish Alternatives]] with an eye toward adding more functionality in the future.

## Callouts
- Callouts work like [Bootstrap Alerts](https://getbootstrap.com/docs/4.0/components/alerts/)
- *[Docs](https://help.obsidian.md/How+to/Use+callouts)*

> [!Info]
> Here's a callout block.

<details>
<summary>additional callout examples</summary>
> [!Warning]
> Here's a callout block.

> [!Note]
> Here's a callout block.

> [!Tip]
> Here's a callout block.

> [!Quote]
> Here's a callout block.

> [!Question]
> Here's a callout block.
</details>


## Custom CSS
- `⌥⌘+I` = `Option+Command+I` = Open inspector (for CSS, etc.)
- How to find elements to adjust ([link](https://forum.obsidian.md/t/identifying-css-selectors/31577))

## Embed searches/queries
- [Search Docs](https://help.obsidian.md/Plugins/Search)
- Requested feature for [sort](https://forum.obsidian.md/t/explicit-sort-parameter-in-query-syntax/11074/15) in queries
- Example query for `Obsidian`:

```query
Obsidian
```

## Graph View
- filter path: `path:"Reading Notes"` or `-path:"Daily Notes" -path:"NABRE"`

## Some Resources
- [Eric Gregorich's Website](https://ericgregorich.com/Home), built all with Obsidian Publish
- [How I Use Daily Notes](https://forum.obsidian.md/t/how-i-use-daily-notes/3057)
- [Automating My Daily Notes with Obsidian](https://www.jamierubin.net/2021/02/08/automating-my-daily-notes-with-obsidian/)
- [21 Day Publish Challenge](https://publish.obsidian.md/alexisrondeau/21-Day+Obsidian+Publish+Challenge)
- [Linking Your Thinking Resources](https://forum.obsidian.md/t/linking-your-thinking-resources/6177)
- [Andy Matuschak Notes](https://notes.andymatuschak.org/About_these_notes)
- [Jamie Todd Rubin](https://www.jamierubin.net/2021/01/31/notes-with-obsidian-my-initial-impressions/) (has lots of Obsidian commentary)
- [ ] finish #watch (1 hr) for meta templater for all categories of article/book/etc. [3 Amazing Obsidian Plugins [[DataView]], [[Outliner]], & [[Templater]] - YouTube](https://youtu.be/2234DXKbNgM?t=2935)
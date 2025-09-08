---
publish: true
---
# Shortcuts

### Mac Keys
| Key          | Symbol |
| ------------ | ------ |
| Command      | ⌘      |
| Shift        | ⇧      |
| Option (Alt) | ⌥      |
| Control      | ⌃      |
| Caps Lock    | ⇪      |
| Tab          | ⇥      |

## Slack
- `⌘+⇧+U` - hyperlink (since you can't ⌘+K in Slack), or just highlight the text and paste the url on top of it
- `⇧ + esc` - `shift - esc` - clear all unread
 

## Obsidian
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
- `⌃ + ⇥ = ctrl + tab` - cycle tabs forward
- `⌃ + ⇧ + ⇥ = ctrl + shift + tab` - cycle tabs reverse
- `⌘+-/0` - zoom in/out

## Mac
- `shift + option + 8` = ° (degree symbol)
- `⌥ + x` = `option + x` = ≈ (or use Espanso `\approx`)
- `⌃ + ⌘ + space` = `ctrl + cmd + space` = → (opens character viewer)
- `⌃ + ⌘ + Q` = `ctrl + cmd + Q` = Lock screen
- `drutil tray eject` - eject CD
- `⌘+Shift+.` - show hidden files in Finder
- `⌘ + ⇧ + 5` = `cmd + shift + 5` = open screenshot tool (save to preview to annotate)
- `option + -` - en-dash (–)
- `shift + option + -` - em-dash (—)
- `⌘ + ⌥ + H` - minimize all windows except current 


### [**ScreenBrush**](https://imagestudiopro.com/screenbrush/)
- `⌥ + tab` = `option + tab` - draw on screen


## Excel
- `⌘ + T` = `cmd + T` - Absolute/relative references
- `⌃ + ⌥ + tab` = `ctrl + option + tab` - indent
- `⌘ + R/D` = `cmd + R/D` - fill formula right/down
- `crtl + shift + 9` - expand grouped cells? (play with it)
- `⌘ + ⇧ + F` - `cmd + shift + F` - filter
- select 0,1 and drag to get 0,1,2,3,etc.
- `⇧ + fn + F9` = `shift + function + F9` - calculate sheet
- `⌘ + ⇧ + T` = `cmd + shift + T` - auto-sum column


## Google Sheets
- `fn + F4` = Absolute/relative references
- `cmd + shift + E` = center
- `option + ↓` or `cmd + →` - switch tabs/sheets 
- Data > Data Connectors > Refresh Options > Refresh All
- `option + shift + →` - group rows/cols
- ...
- =INDEX(Forecast!$AN:$AN,match(1,(Forecast!$J:$J=F$50)*(Forecast!$E:$E=$A52)*(Forecast!$I:$I=$B52),0),1)
- =SUMPRODUCT(($Q262:$AO262=AB266)*$Q263:$AO263)
- =query(A1:D51,"Order by C Desc Limit 10")
- =IMPORTRANGE("https://docs.google.com/spreadsheets/d/1rzwxJdrlnjJi_mpUiE8cBQFQKBkzcLHK1hsUNvLcdPE/edit#gid=1198758696","'Upcoming Deals'!A2:K20")
- filter with "all" condition from [here](https://docs.google.com/spreadsheets/d/1P_TGwjaFRzQ4SAaUxfxF--eBQGWyfddbbDcxeg9IGk8/edit#gid=1138395796):
	- `countifs(Data!$F$3:$F,$B7,Data!$H$3:$H,IF($C$1="All","<>""",$C$1),Data!$B$3:$B,IF($C$2="All","<>""",$C$2),Data!$E$3:$E,F$5)`
- unpivot using `ARRAYFORMULA(SPLIT(FLATTEN(`: [How to Unpivot Data in Google Sheets](https://dataful.tech/google-sheets/formulas/how-to-unpivot/) and [Unpivot in Google Sheets with FLATTEN: Column pairs, auto expand++ - YouTube](https://youtu.be/lCB6aXcQdV4)
- Formats: 
	- `"$"#,##0,"K";"$"-#,##0,"K";--`
	- `"$"#,##0.0,,"M";-"$"#,##0.0,,"M";--`
	- `"$"#,##0.0,,,"B";-"$"#,##0.0,,,"B";--`
- Sparkline: `=sparkline(L10:L15,{"charttype","column";"ymin",0})`
## PyCharm
- `⌘ + ⇧ + 8` - `cmd + shift + 8` - multi-select (or just Shift and arrow)
- `⌥ + ⌘ + L` - `option + command + L` - format lines
- `⇧ + ⌘ + L` - `shift + command + L` - open new SQL console 
- `⌃ + G` - `ctrl + G` - command + D sublime equivalent to select next occurrence
- `⌥ + ⇧ + ↑` - `option + shift + up arrow` - move lines up
- `⇧ + ⌥ + ⌘ + select` - `shift + option + command + select` - multi-select
- `shift + command + ;` - run [[Mac Computer Setup#^573833|Black]] formatting
- `⌘ + home/end` - `cmd + home/end` - jump to top/bottom of file
- control + shift + R to run
- control + J twice to pull up docs for function
- Launch jupyter notebook: right click on project folder > new > jupyter notebook
- click red dot in gutter for debugging break point
- When editing HTML: View > Open In Browser


## Gmail
*[Keyboard shortcuts for Gmail](https://support.google.com/mail/answer/6594?hl=en&co=GENIE.Platform=Desktop#zippy=%2Capplication%2Cnavigation%2Cactions)*
- search: `in:inbox label:.pws`
- search: `category:social , older_than:2y`
- search: `larger:10M after:2021/11/3 before:2023/11/4 `
- search: `size:25mb older_than:1y `
- `a` - reply all
- `shift + u` - mark as unread
- `u` - return to inbox
- `b` - snooze
- `#` - delete
- `g + n` and `g + p` - to go to next/previous page 
- `/` - search mail


## Terminal
- `ls -l` - list files with permissions (i.e. `chmod +x`)


## Vimium 
[Vimium-FF – Shortcuts](https://addons.mozilla.org/en-US/firefox/addon/vimium-ff/)
- `gs` - open source 
- `yy` - copy url to clipboard 
- `d` and `u` - scroll up/down half page 


## GCP 
- `option + ⬆` - move line up/down
- `cmd + click` on a table name to get it's details 

7-day history for tables. For views, need to get source tables 
```sql
SELECT   * FROM 
`table` 
FOR SYSTEM_TIME AS OF TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 30 MINUTE)
```
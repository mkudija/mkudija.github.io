---
publish: true
---

# Mac Computer Setup

## Applications
- Firefox
	- [Bitwarden](https://addons.mozilla.org/en-US/firefox/addon/bitwarden-password-manager/)
	- [Vimium](https://addons.mozilla.org/en-US/firefox/addon/vimium-ff/)
	- [uBlock Origin](https://addons.mozilla.org/en-GB/firefox/addon/ublock-origin/)
	- [LocalCDN](https://addons.mozilla.org/en-US/firefox/addon/localcdn-fork-of-decentraleyes/)
	- [ClearURLs](https://addons.mozilla.org/en-US/firefox/addon/clearurls/)
	- [Copy as Markdown](https://addons.mozilla.org/en-GB/firefox/addon/copy-as-markdown/) (supplemented by [[Obsidian#obsidian-auto-link-title https github com zolrath obsidian-auto-link-title]] plugin)
	- [LaTeX in Slack](https://addons.mozilla.org/en-US/firefox/addon/latex-in-slack/)
	- [Minimal Twitter](https://addons.mozilla.org/en-GB/firefox/addon/min-twitter/)
	- [Disable Javascript](https://addons.mozilla.org/en-GB/firefox/addon/disable-javascript/)
	- [Font Finder](https://addons.mozilla.org/en-GB/firefox/addon/font-inspect/)
- Safari
	- [Vimari: Safari port of vimium](https://github.com/televator-apps/vimari)
- [[Obsidian]] ([link](https://obsidian.md/))
- Utilities
	- [Bitwarden](https://bitwarden.com/)
	- [Dropbox](https://www.dropbox.com/downloading)
	- [Espanso](https://espanso.org/install/) 
		- [[Espanso default.yml]] (access via `espanso path` or `espanso edit`) ([example 1](https://github.com/Lissy93/espanso-config/blob/master/utils.yml), [example 2](https://github.com/ekiel/espanso/blob/master/default.yml))
		- *need to [install brew](https://stackoverflow.com/questions/66666134/how-to-install-homebrew-on-m1-mac)*
		- double tap option (⌥) to enable/disable Espanso (can turn this toggle key behavior off-[link](https://espanso.org/docs/next/configuration/options/))
		- ~~[[Keyboard Maestro]]~~ (replaced by Espanso)
	- [Spectacle](https://www.spectacleapp.com/)
	- [Shortcat](https://shortcatapp.com/) ([how to use](https://superuser.com/questions/93937/keyboard-shortcut-to-right-click-in-mac-os-x/715116))
	- [Itsycal](https://www.mowglii.com/itsycal/)
		- `yyyy-MM-dd E ✈ h:mm a`
	- [WeatherBug](https://apps.apple.com/us/app/weatherbug-weather-forecasts-and-alerts/id1059074180?mt=12)
	- [Dozer](https://github.com/Mortennn/Dozer)
		- `brew install --cask dozer`
	- [ScreenBrush](https://imagestudiopro.com/screenbrush/)
		- option-tab to enable
	- [Boop](https://boop.okat.best/)
	- [Fig](https://fig.io/)
- [Signal](https://signal.org/download/)
- [GitHub Desktop](https://desktop.github.com/)
- [iTerm2](https://iterm2.com/downloads.html)
	- Set up iTerm2 shortcut keys: [Link](https://stackoverflow.com/questions/6205157/iterm-2-how-to-set-keyboard-shortcuts-to-jump-to-beginning-end-of-line#10485061)
- [PyCharm](https://www.jetbrains.com/pycharm/download/#section=mac)
	- [Black](https://black.readthedocs.io/en/stable/getting_started.html#installation) code formatter setup in PyCharm: ^573833
		- Install: `pip install black`
		- Set up in PyCharm ([Black docs](https://black.readthedocs.io/en/stable/integrations/editors.html#pycharm-intellij-idea)): PyCharm > Preferences > Tools > External tools
			- Name: `Black`
			- Description: `The uncompromising code formatter`
			- Program: `/Users/matthewkudija/.pyenv/versions/3.10.0/lib/python3.10/site-packages/black` (install in some base environment that won't get touched)
			- Arguments: `"$FilePath$"`
			- Working Directory: `$ProjectFileDir$`
		- Change Black file permissions (so PyCharm can execute it):
			- `chmod ugo+x /Users/matthewkudija/.pyenv/versions/3.10.0/lib/python3.10/site-packages/black`
				- user, group, other, + x can execute 
		- Set up PyCharm shortcut: PyCharm > Preferences > Keymap > `shift + command + ;`
		- Usage: `black <path_to_file>`
- [Sublime text](https://www.sublimetext.com/download)
- [TexShop](https://pages.uoregon.edu/koch/texshop/obtaining.html)
	- requires [MacTeX - TeX Users Group](https://tug.org/mactex/mactex-download.html) (`MacTeX.pkg`, did not work with basic version)
	- then download - [Latest TeXShop, Version 4.76](https://pages.uoregon.edu/koch/texshop/texshop-64/texshop.zip) for Intel and Arm on Sierra and higher (55.6 MB)
- [Fig](https://fig.io/)
- Flycut
- Python
	- Install Homebrew
		- `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"`
	- Install pip
		- `curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py`
		- `python get-pip.py` or `python3 get-pip.py`
	- Install pyenv
		- `brew update`
		- `brew install pyenv`
		- `pyenv init`
	- Install python
		- ==`brew install xz` (to prevent issues with lzma after installing python)==
		- `pyenv install -v <python-version>` i.e. `pyenv install -v 3.10.1`
			- see available versions with `pyenv install --list`
		- `pyenv local 3.10.1`
		- `pyenv versions` to confirm that `*` is by `3.10.1`
		- `pyenv init --path`, then run the output of that, like `export PATH="/Users/matthewkudija/.pyenv/shims:${PATH}"`
		- Confirm version by running `which python` or `python`
		- [[Manage pipenv environments]]
		- install packages, i.e. `pip install pandas`
	- Manage versions 
		- `pyenv versions` - see available versions
		- `pyenv install 3.10.0` - install version
		- `pyenv shell <version>`- select version just for current shell session
		- `pyenv local <version>`- automatically select whenever you are in the current directory (or its subdirectories)
	- `pyenv global <version>`- select globally for your user account
- Old/other
	- [Duplicati](https://www.duplicati.com/) (from [Kev](https://kevq.uk/my-home-server-2-months-on/))


## Root-specific
*[Root link](https://docs.google.com/document/d/13zLLKRXPQd75kkDyANanYz5V-CPN1GyqtBOVZcryIVk/edit#)*

- [Microsoft Office](https://joinroot.askspoke.com/next/knowledge/5f2c604194d10d00062ab421)
	- Excel WST Plugin: [Link](http://www.wallst-training.com/about/resources.html)
- [Google File Stream](https://support.google.com/a/answer/7491144?hl=en#zippy=%2Cmac)
- [AWS VPN](https://docs.google.com/document/d/1WNxQLoIm-j1rjQQ60CULNUtb1AIFbX4TGeg9orQRtFc/edit)
- [Yubikey Manager](https://joinroot.askspoke.com/next/knowledge/5de56f0c3122eb00079d0b1d) (so it doesn’t make cccccckvurecrlvudbdrurvbufrihlurtthrbrvclfri when you tap your keys)

---
Created: [[2021-07-19-Mon]]
Updated: <%+ tp.file.last_modified_date("YYYY-MM-DD-ddd") %>

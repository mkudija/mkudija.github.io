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
	- [Copy as Markdown](https://addons.mozilla.org/en-GB/firefox/addon/copy-as-markdown/)
	- [LaTeX in Slack](https://addons.mozilla.org/en-US/firefox/addon/latex-in-slack/)
	- [Minimal Twitter](https://addons.mozilla.org/en-GB/firefox/addon/min-twitter/)
	- [Disable Javascript](https://addons.mozilla.org/en-GB/firefox/addon/disable-javascript/)
	- [Font Finder](https://addons.mozilla.org/en-GB/firefox/addon/font-inspect/)
- [[Obsidian]] ([link](https://obsidian.md/))
- Utilities
	- [Bitwarden](https://bitwarden.com/)
	- [Dropbox](https://www.dropbox.com/downloading)
	- [Espanso](https://espanso.org/install/) 
		- [[Espanso default.yml]] (access via `espanso path` or `espanso edit`) ([example 1](https://github.com/Lissy93/espanso-config/blob/master/utils.yml), [example 2](https://github.com/ekiel/espanso/blob/master/default.yml))
		- *need to [install brew](https://stackoverflow.com/questions/66666134/how-to-install-homebrew-on-m1-mac)*
		- double tap option (⌥) to enable/disable espanso (can turn this toggle key behavior off-[link](https://espanso.org/docs/next/configuration/options/))
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
- [Sublime text](https://www.sublimetext.com/download)
- [Fig](https://fig.io/)
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

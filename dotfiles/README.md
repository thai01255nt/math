# Setup terminal
## 1. Make beautiful window profile
### Follow by [devaslife](https://www.youtube.com/watch?v=5-aK2_WwrmM)
####
- Font: [Nerd fonts](https://github.com/ryanoasis/nerd-fonts) (I'm using hack font)
- Open settings and enable acrylic material for both 
- Color theme is modded from One-Half Dark theme, change background to **#001B26**
## 2. Using linux throught wsl
## Ubuntu
### Fish shell theme: inspired by devaslife
```
# install fish
# get last new version fish >= 3.4
sudo apt-add-repository ppa:fish-shell/release-3
sudo apt-get install fish
# open fish shell and set default shell
fish
chsh -s /usr/bin/fish
# To config your theme
fish_config browse
```
### Theme
[oh my posh](https://ohmyposh.dev/docs/installation/linux)
```
# Make fish using oh my posh
oh-my-posh init fish | source
exec fish
# For the theme, you can choose another theme
# custom.omp.json is symlinked from this repo (see "Link dotfiles" below)
oh-my-posh init fish --config ~/.config/oh-my-posh/custom.omp.json | source
```
### Tmux
Config is split per environment: `tmux.conf` (common) sources `wsl.conf` / `linux.conf` / `macos.conf`
(clipboard `copy-command`: clip.exe / wl-copy or xclip / pbcopy).
```
# ~/.config/tmux is symlinked from this repo (see "Link dotfiles" below)
tmux source ~/.config/tmux/tmux.conf
```
#### [ide](./.scripts/ide) command for fast split tmux pane
Symlinked to `~/.local/bin/ide` in "Link dotfiles" below (no sudo needed).
### Git
# if using these configs, need install peco for query git hist 
### Fish
## Ingredients:
- fish
- [fisher](https://github.com/jorgebucaran/fisher) (plugin manager for fish)
- shellder (optional): theme 
```
fisher install simnalamburt/shellder
sudo apt install fzf
sudo apt install fd-find
sudo apt install bat
mkdir -p ~/.local/bin
ln -s /usr/bin/batcat ~/.local/bin/bat
fisher install PatrickF1/fzf.fish
```
- [fzf.fish](https://github.com/PatrickF1/fzf.fish): finding ```fisher install PatrickF1/fzf.fish```
- nerd fonts
- z: plugin for directory jumping ```fisher install jethrokuan/z```
- peco: filtering tool
- eza (exa on macos): alternative for ls
- ghq (not used): Local Git repository organizer
```
### Link dotfiles
Configs are **symlinked** to this repo (clone it to `~/math`), so editing them edits the repo: commit/push to sync.
Don't move/delete `~/math` (links break). Existing files are backed up to `~/.dotfiles-backup`.
```
R=~/math/dotfiles; B=~/.dotfiles-backup; mkdir -p $B ~/.config/fish ~/.config/oh-my-posh ~/.local/bin
link() { [ -e "$2" ] && [ ! -L "$2" ] && mv "$2" "$B/"; ln -sfn "$1" "$2"; }
link $R/tmux ~/.config/tmux
for f in config.fish config-linux.fish config-osx.fish config-windows.fish; do link $R/fish/$f ~/.config/fish/$f; done
link $R/custom.omp.json ~/.config/oh-my-posh/custom.omp.json
link $R/.scripts/ide ~/.local/bin/ide   # tmux pane layout command
# WSL only (agent-manager notify, see personals/AGENT-MANAGER.md)
link $R/agent-manager/am-notify ~/.local/bin/am-notify
link $R/agent-manager/powershell.exe ~/.local/bin/powershell.exe
# check
ls -l ~/.config/tmux ~/.config/fish/config*.fish ~/.config/oh-my-posh/custom.omp.json ~/.local/bin/am-notify
```
Only the 4 fish config files are linked; `functions/`, `conf.d/`, `fish_variables` stay local.
Machine-specific fish settings go in `~/.config/fish/config-local.fish` (not in repo).
```

#
:lua =require('vim.lsp.log').get_filename()
```

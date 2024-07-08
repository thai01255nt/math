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
chsh -s /user/bin/fish
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
# make file custom.omp.json in ~/.config/oh-my-posh and run
oh-my-posh init fish --config ~/.config/oh-my-posh/custom.omp.json | source
```
### Alias
```
# Aliases
alias g="git"
alias vim="nvim"

alias ls="ls -p -G"
alias la="ls -A"
alias lla="ll -A"
```
### Tmux
```
# create tmux conf and source
tmux source ~/.config/tmux/tmux.conf
```
#### create [ide](./dotfiles/.scripts/ide) command for fast split tmux pane
```
cp ./dotfiles/.scripts/ide /user/bin
```
### Git
# if using these configs, need install peco for query git hist 
### Fish
## Ingredients:
- fish
- [fisher](https://github.com/jorgebucaran/fisher) (plugin manager for fish)
- shellder (optional): theme ```fisher install simnalamburt/shellder```
- nerd fonts
- z: plugin for directory jumping ```fisher install jethrokuan/z```
- peco: filtering tool
- eza (exa on macos): alternative for ls
- ghq (optional): Local Git repository organizer
```
# add fish config
cat ./dotfiles/fish/config-linux.fish >> ~/.config/fish/config-linux.fish
cat ./dotfiles/fish/config-osx.fish >> ~/.config/fish/config-osx.fish
cat ./dotfiles/fish/config-window.fish >> ~/.config/fish/config-window.fish
cat ./dotfiles/fish/config.fish >> ~/.config/fish/config.fish

```

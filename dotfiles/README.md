# Setup terminal
## 1. Make beautiful window profile
### Follow by [devaslife](https://www.youtube.com/watch?v=5-aK2_WwrmM)
####
- Font: [Nerd fonts](https://github.com/ryanoasis/nerd-fonts) (I'm using hack font)
- Open settings and enable acrylic material for both 
- Color theme is modded from One-Half Dark theme, change background to **#001B26**
## 2. Using linux throught wsl
## Ubuntu
### Fish shell: inspired by devaslife
```
# install fish
# get last new version fish >= 3.4
sudo apt-add-repository ppa:fish-shell/release-3
sudo apt-get install fish
# open fish shell and set default shell
fish
chsh -s /user/bin/fish
```
### Theme
[oh my posh](https://ohmyposh.dev/docs/installation/linux)
```
# Make fish using oh my posh
oh-my-posh init fish | source
exec fish
# For the theme, you can choose another theme
# make file custom.omp.json in ~/.config/fish and run
oh-my-posh init fish --config ~/jandedobbeleer.omp.json | source
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
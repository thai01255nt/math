# install scoop
iwr -useb get.scoop.sh | iex
scoop install curl sudo jq

# install git
winget install -e --id Git.Git

# install neovim
scoop install neovim

# cd into user folder config alias for shell

mkdir .config/powershell
nvim .config/powershell/user_profile.ps1
nvim $Prof

# oh-my-posh
Install-Module posh-git -Scope CurrentUser -Force
Install-Module oh-my-posh -Scope CurrentUser -Force


# install scoop
iwr -useb get.scoop.sh | iex
scoop install curl sudo jq

# install git
winget install -e --id Git.Git

# install neovim
scoop install neovim

# cd into user folder config alias for shell
cp dotfiles\.gitconfig $Home\.gitconfig

mkdir $Home\.config\powershell
cp dotfiles\powershell\user_profile.ps1 $Home\.config\powershell\user_profile.ps1
cp dotfiles\powershell\Microsoft.PowerShell_profile.ps1 $PROFILE.CurrentUserAllHosts
cp dotfiles\custom.omp.json $Home\.config\powershell\custom.omp.json

# oh-my-posh
Install-Module posh-git -Scope CurrentUser -Force
Install-Module oh-my-posh -Scope CurrentUser -Force

# nodejs
scoop install nvm
nvm install lts

# icon terminal
Install-Module -Name Terminal-Icons -Repository PSGallery -Force
#Import-Module Terminal-Icons
Install-Module -Name z -Force
Install-Module -Name PSReadLine -AllowPrerelease -Scope CurrentUser -Force -SkipPublisherCheck
#Set-PSReadLineOption -PredictionSource History
#Set-PSReadLineOption -PredictionViewStyle ListView

# fuzzy finder
scoop install fzf
Install-Module -Name PSFzf -Scope CurrentUser -Force
scoop install fd
scoop install bat
#Set-PsFzOption -PSReadlineChordProvider 'Ctrl+f' -PSReadlineChordReverseHistory 'Ctrl+r'

# lazy-vim
git clone git@github.com:thai01255nt/lazy-vim.git  $env:LOCALAPPDATA\nvim
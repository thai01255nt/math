```
sudo apt-get install build-essential

# START
sudo apt-add-repository ppa:fish-shell/release-3
sudo apt-get install fish
chsh -s /usr/bin/fish
exec fish
sudo apt install lazygit
mkdir ~/.config/tmux
mkdir ~/.config/oh-my-posh
set SOURCE_CONFIG_FOLDER=dotfiles
cp -a fish/. ~/.config/fish/
cp -a tmux/. ~/.config/tmux/
cp .scripts/ide /usr/bin/
cp custom.omp.json ~/.config/oh-my-posh
cp .gitconfig ~/.gitconfig
tmux source ~/.config/tmux/tmux.conf
curl -sL https://raw.githubusercontent.com/jorgebucaran/fisher/main/functions/fisher.fish | source && fisher install jorgebucaran/fisher
fisher install jorgebucaran/nvm.fish
sudo apt install fzf
sudo apt install fd-find
sudo apt install bat
mkdir -p ~/.local/bin
ln -s /usr/bin/batcat ~/.local/bin/bat
fisher install PatrickF1/fzf.fish
fisher install jethrokuan/z

# PECO
sudo apt install peco

#EZA
sudo mkdir -p /etc/apt/keyrings
wget -qO- https://raw.githubusercontent.com/eza-community/eza/main/deb.asc | sudo gpg --dearmor -o /etc/apt/keyrings/gierens.gpg
echo "deb [signed-by=/etc/apt/keyrings/gierens.gpg] http://deb.gierens.de stable main" | sudo tee /etc/apt/sources.list.d/gierens.list
sudo chmod 644 /etc/apt/keyrings/gierens.gpg /etc/apt/sources.list.d/gierens.list
sudo apt update
sudo apt install -y eza
sudo apt-get install ripgrep
```

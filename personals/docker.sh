```
apt update
apt-add-repository ppa:fish-shell/release-3
apt-get install -y build-essential curl unzip fish wget
curl -s https://ohmyposh.dev/install.sh | bash -s -- -d /usr/bin

# START
chsh -s /usr/bin/fish
exec fish
fish_config theme save 'Solarized Dark'
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
apt -y install fzf fd-find bat peco
mkdir -p ~/.local/bin
ln -s /usr/bin/batcat ~/.local/bin/bat
fisher install PatrickF1/fzf.fish
fisher install jethrokuan/z


#EZA
mkdir -p /etc/apt/keyrings
wget -qO- https://raw.githubusercontent.com/eza-community/eza/main/deb.asc | gpg --dearmor -o /etc/apt/keyrings/gierens.gpg
echo "deb [signed-by=/etc/apt/keyrings/gierens.gpg] http://deb.gierens.de stable main" | tee /etc/apt/sources.list.d/gierens.list
chmod 644 /etc/apt/keyrings/gierens.gpg /etc/apt/sources.list.d/gierens.list
apt update
apt-get install -y eza
apt-get install -y ripgrep
```

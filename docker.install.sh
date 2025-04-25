#!/bin/fish
# font
wget https://github.com/ryanoasis/nerd-fonts/releases/download/v3.4.0/Hack.tar.xz
tar -xvf Hack.tar.xz -o HackNerdFontMono-Regular.ttf
mkdir ~/.local/share/fonts
cp HackNerdFontMono-Regular.ttf ~/.local/share/fonts/HackNerdFontMono-Regular.ttf
cp HackNerdFontMono-Regular.ttf /usr/local/share/fonts/HackNerdFontMono-Regular.ttf
rm HackNerdFontMono-Regular.ttf

yes | fish_config theme save 'Solarized Dark'
cd dotfiles
mkdir ~/.config/tmux
mkdir ~/.config/oh-my-posh
set SOURCE_CONFIG_FOLDER dotfiles
cp -a fish/. ~/.config/fish/
cp -a tmux/. ~/.config/tmux/
cp .scripts/ide /usr/bin/
cp custom.omp.json ~/.config/oh-my-posh
cp .gitconfig ~/.gitconfig
curl -sL https://raw.githubusercontent.com/jorgebucaran/fisher/main/functions/fisher.fish | source && fisher install jorgebucaran/fisher
fisher install jorgebucaran/nvm.fish
apt -y install fzf fd-find bat peco
mkdir -p ~/.local/bin
ln -s /usr/bin/batcat ~/.local/bin/bat
fisher install PatrickF1/fzf.fish
fisher install jethrokuan/z

#EZA
mkdir -p /etc/apt/keyrings
wget -qO- https://raw.githubusercontent.com/eza-community/eza/main/deb.asc | gpg --dearmor -o -y /etc/apt/keyrings/gierens.gpg
echo "deb [signed-by=/etc/apt/keyrings/gierens.gpg] http://deb.gierens.de stable main" | tee /etc/apt/sources.list.d/gierens.list
chmod 644 /etc/apt/keyrings/gierens.gpg /etc/apt/sources.list.d/gierens.list
apt update
apt-get install -y eza
apt-get install -y ripgrep

#neovim
curl -LO https://github.com/neovim/neovim/releases/latest/download/nvim-linux-x86_64.tar.gz
rm -rf /opt/nvim
tar -C /opt -xzf nvim-linux-x86_64.tar.gz
mv /opt/nvim-linux-x86_64 /opt/nvim-linux64
rm nvim-linux-x86_64.tar.gz
apt -y install git
git clone https://github.com/thai01255nt/lazy-vim.git ~/.config/nvim

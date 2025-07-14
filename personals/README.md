```
sudo apt-get install -y build-essential tmux curl git

wget https://github.com/ryanoasis/nerd-fonts/releases/download/v3.4.0/Hack.tar.xz
tar -xvf Hack.tar.xz HackNerdFontMono-Regular.ttf
mkdir -p ~/.local/share/fonts
cp HackNerdFontMono-Regular.ttf ~/.local/share/fonts
fc-cache -fv
rm Hack.tar.xz
rm HackNerdFontMono-Regular.ttf

# START
LAZYGIT_VERSION=$(curl -s "https://api.github.com/repos/jesseduffield/lazygit/releases/latest" | \grep -Po '"tag_name": *"v\K[^"]*')
curl -Lo lazygit.tar.gz "https://github.com/jesseduffield/lazygit/releases/download/v${LAZYGIT_VERSION}/lazygit_${LAZYGIT_VERSION}_Linux_x86_64.tar.gz"
tar xf lazygit.tar.gz lazygit
sudo install lazygit -D -t /usr/local/bin/
rm lazygit.tar.gz
rm -rf lazygit
sudo apt-add-repository -y ppa:fish-shell/release-3
sudo apt-get install -y fish
chsh -s /usr/bin/fish
exec fish

git clone https://github.com/thai01255nt/math.git
cd math
mkdir ~/.config/tmux
mkdir ~/.config/oh-my-posh
cp -a ./dotfiles/fish/. ~/.config/fish/
cp -a ./dotfiles/tmux/. ~/.config/tmux/
sudo cp ./dotfiles/.scripts/ide /usr/bin/
cp ./dotfiles/custom.omp.json ~/.config/oh-my-posh
cp ./dotfiles/.gitconfig ~/.gitconfig
# tmux source ~/.config/tmux/tmux.conf
curl -s https://ohmyposh.dev/install.sh | sudo bash -s -- -d /usr/bin
curl -sL https://raw.githubusercontent.com/jorgebucaran/fisher/main/functions/fisher.fish | source && fisher install jorgebucaran/fisher
fisher install jorgebucaran/nvm.fish
sudo apt install -y fzf fd-find bat
mkdir -p ~/.local/bin
ln -s /usr/bin/batcat ~/.local/bin/bat
fisher install PatrickF1/fzf.fish
fisher install jethrokuan/z

# PECO
sudo apt install -y peco

#EZA
sudo mkdir -p /etc/apt/keyrings
wget -qO- https://raw.githubusercontent.com/eza-community/eza/main/deb.asc | sudo gpg --dearmor -o /etc/apt/keyrings/gierens.gpg
echo "deb [signed-by=/etc/apt/keyrings/gierens.gpg] http://deb.gierens.de stable main" | sudo tee /etc/apt/sources.list.d/gierens.list
sudo chmod 644 /etc/apt/keyrings/gierens.gpg /etc/apt/sources.list.d/gierens.list
sudo apt update
sudo apt install -y eza
sudo apt-get install ripgrep

# lazy vim
git clone https://github.com/thai01255nt/lazy-vim.git ~/.config/nvim
curl -LO https://github.com/neovim/neovim/releases/latest/download/nvim-linux-x86_64.tar.gz
sudo rm -rf /opt/nvim
sudo tar -C /opt -xzf nvim-linux-x86_64.tar.gz
sudo mv /opt/nvim-linux-x86_64 /opt/nvim-linux64
rm nvim-linux-x86_64.tar.gz
nvm install lts
nvm use lts
npm install -g yarn
```

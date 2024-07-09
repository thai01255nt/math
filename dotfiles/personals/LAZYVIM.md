# Install neovim, follow lazyvim to setup theme, telescope,...
```
# required
mv ~/.config/nvim{,.bak}

# optional but recommended
mv ~/.local/share/nvim{,.bak}
mv ~/.local/state/nvim{,.bak}
mv ~/.cache/nvim{,.bak}
git clone https://github.com/LazyVim/starter ~/.config/nvim
rm -rf ~/.config/nvim/.git

# run neovim to init and install plugins
# install build-essential before run that
sudo apt update
sudo apt install build-essential
nvim init.lua
```


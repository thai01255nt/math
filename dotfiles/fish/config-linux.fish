if type -q eza
    alias ll "eza -l -g --icons"
    alias lla "ll -a"
end
export PATH="$PATH:/opt/nvim-linux64/bin"
command -qv nvim && alias vim nvim

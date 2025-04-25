cd dotfiles
apt update
apt install -y software-properties-common
apt-add-repository -y ppa:fish-shell/release-3
apt-get install -y build-essential curl unzip fish wget
curl -s https://ohmyposh.dev/install.sh | bash -s -- -d /usr/bin

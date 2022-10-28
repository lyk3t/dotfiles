# Dotfiles

Dotfiles are organized in a git bare repo, because there is a lot going on in the home directory and I did not like the overhead of maintaining a git ignore (or ''reverse git ignore') for it.

Thus, repo is set up as a bare repo.

To set it up use
```
echo 'alias dotfiles="/usr/bin/git --git-dir=$HOME/.dotfiles/ --work-tree=$HOME"' >> $HOME/.bashrc
. ~/.bashrc
echo ".dotfiles" >> .gitignore
git clone --bare https://github.com/lyk3t/dotfiles.git $HOME/.dotfiles
dotfiles checkout
dotfiles config --local status.showUntrackedFiles no
```

install dependencies via playbook:
```
sudo apt get ansible
ansible-playbook play-dot.yml
```
and follow the finishing steps from the output

### Steps should be obsolete if you follow the ansible way
dependencies can be installed with
```
yay -S zsh tmux fzf
git clone https://github.com/robbyrussell/oh-my-zsh.git ~/.oh-my-zsh
git clone https://github.com/seebi/dircolors-solarized.git ~/.dircolors
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ~/.oh-my-zsh/custom/plugins/zsh-syntax-highlighting
git clone https://github.com/junegunn/fzf.git ~/.oh-my-zsh/custom/plugins/fzf
~/.oh-my-zsh/custom/plugins/fzf/install --bin
git clone https://github.com/Treri/fzf-zsh.git ~/.oh-my-zsh/custom/plugins/fzf-zsh
git clone https://github.com/lukechilds/zsh-nvm ~/.oh-my-zsh/custom/plugins/zsh-nvm

curl -fsSL https://starship.rs/install.sh | bash
chsh -s /usr/bin/zsh

git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm
```


to install nvim and install all plugins from command line use
```
yay -S neovim
curl -fLo ~/.local/share/nvim/site/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
vim +PlugInstall +qall
```

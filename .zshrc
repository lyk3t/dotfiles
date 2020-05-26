# Enable Powerlevel10k instant prompt. Should stay close to the top of ~/.zshrc.
# Initialization code that may require console input (password prompts, [y/n]
# confirmations, etc.) must go above this block, everything else may go below.
if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
  source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
fi

# If you come from bash you might have to change your $PATH.
# export PATH=$HOME/bin:/usr/local/bin:$PATH

# Path to your oh-my-zsh installation.
export ZSH=$HOME/.oh-my-zsh
export MYVIMRC=$HOME/.vimrc
# export DISPLAY=localhost:0

# Set name of the theme to load --- if set to "random", it will
# load a random theme each time oh-my-zsh is loaded, in which case,
# to know which specific one was loaded, run: echo $RANDOM_THEME
# See https://github.com/robbyrussell/oh-my-zsh/wiki/Themes
# ZSH_THEME="agnoster"
ZSH_THEME=powerlevel10k/powerlevel10k
eval `dircolors ~/.dircolors/dircolors.256dark`

# Set list of themes to pick from when loading at random
# Setting this variable when ZSH_THEME=random will cause zsh to load
# a theme from this variable instead of looking in ~/.oh-my-zsh/themes/
# If set to an empty array, this variable will have no effect.
# ZSH_THEME_RANDOM_CANDIDATES=( "robbyrussell" "agnoster" )

# Uncomment the following line to use case-sensitive completion.
# CASE_SENSITIVE="true"

# Uncomment the following line to use hyphen-insensitive completion.
# Case-sensitive completion must be off. _ and - will be interchangeable.
# HYPHEN_INSENSITIVE="true"

# Uncomment the following line to disable bi-weekly auto-update checks.
# DISABLE_AUTO_UPDATE="true"

# Uncomment the following line to automatically update without prompting.
# DISABLE_UPDATE_PROMPT="true"

# Uncomment the following line to change how often to auto-update (in days).
# export UPDATE_ZSH_DAYS=13

# Uncomment the following line if pasting URLs and other text is messed up.
# DISABLE_MAGIC_FUNCTIONS=true

# Uncomment the following line to disable colors in ls.
# DISABLE_LS_COLORS="true"

# Uncomment the following line to disable auto-setting terminal title.
# DISABLE_AUTO_TITLE="true"

# Uncomment the following line to enable command auto-correction.
# ENABLE_CORRECTION="true"

# Uncomment the following line to display red dots whilst waiting for completion.
# COMPLETION_WAITING_DOTS="true"

# Uncomment the following line if you want to disable marking untracked files
# under VCS as dirty. This makes repository status check for large repositories
# much, much faster.
# DISABLE_UNTRACKED_FILES_DIRTY="true"

# Uncomment the following line if you want to change the command execution time
# stamp shown in the history command output.
# You can set one of the optional three formats:
# "mm/dd/yyyy"|"dd.mm.yyyy"|"yyyy-mm-dd"
# or set a custom format using the strftime function format specifications,
# see 'man strftime' for details.
# HIST_STAMPS="mm/dd/yyyy"

# Would you like to use another custom folder than $ZSH/custom?
# ZSH_CUSTOM=/path/to/new-custom-folder

# Which plugins would you like to load?
# Standard plugins can be found in ~/.oh-my-zsh/plugins/*
# Custom plugins may be added to ~/.oh-my-zsh/custom/plugins/
# Example format: plugins=(rails git textmate ruby lighthouse)
# Add wisely, as too many plugins slow down shell startup.
plugins=(git tmux zsh-syntax-highlighting zsh-nvm fzf-zsh ripgrep)

source $ZSH/oh-my-zsh.sh

# User configuration

# export MANPATH="/usr/local/man:$MANPATH"

# You may need to manually set your language environment
# export LANG=en_US.UTF-8

# Preferred editor for local and remote sessions
# if [[ -n $SSH_CONNECTION ]]; then
#   export EDITOR='vim'
# else
#   export EDITOR='mvim'
# fi

# Compilation flags
# export ARCHFLAGS="-arch x86_64"

# environments
# export FZF_DEFAULT_COMMAND='rg --files --hidden --follow --glob "!.git/*"'
export FZF_DEFAULT_COMMAND='rg --files --no-ignore --hidden --follow --glob "\!.git/*" --glob "\!node_modules/*"'
export PATH=$PATH:$HOME/.local/bin:$HOME/dev/flutter/bin
export DOCKER_HOST=tcp://localhost:2375
# functions
# short scripts that are not exluded in a own file
startssh() {
eval "$(ssh-agent -s)"
ssh-add 
}

cloudia() {
  (cd /d/dev/cloudia && code .) >/dev/null
}

sam() {
  (cd /d/dev/sam && code .) >/dev/null
}

mfb() {
  (cd /d/dev/mfb-cs/mfb_cs/f && code .) >/dev/null
}

emailsvc() {
  (cd /d/dev/email-service && code .) >/dev/null
}

getOrderContent(){
if [ "$1" != "" ]; then
  scp -r 10.21.14.65:/var/spool/boc_order/$1 /d/orders
  explorer.exe "D:\\orders\\$1"
else
  echo "You have to provide the order timestamp to identify the necessary dir"
fi
}

# trello post functions (calls python script)
# new maintenance
newmain(){
  /d/dev/allMyLittleScripts/createNewTrelloCard.py maintenance "$@"
}

# new appointment
newapp(){
  /d/dev/allMyLittleScripts/createNewTrelloCard.py appointment "$@"
}

# new deadline
deadline(){
  /d/dev/allMyLittleScripts/createNewTrelloCard.py deadline "$@"
}

# remove user and workstation from prompt
prompt_context() {}

# Set personal aliases, overriding those provided by oh-my-zsh libs,
# plugins, and themes. Aliases can be placed here, though oh-my-zsh
# users are encouraged to define aliases within the ZSH_CUSTOM folder.
# For a full list of active aliases, run `alias`.
#
#
# Example aliases
# alias zshconfig="mate ~/.zshrc"
# alias ohmyzsh="mate ~/.oh-my-zsh"
alias dev="cd /d/dev"
alias vscode="/mnt/c/Program\ Files/Microsoft\ VS\ Code/Code.exe"
alias ls='ls --color=auto'
alias -g grep='grep --color=auto'
alias -g fgrep='fgrep --color=auto'
alias -g egrep='egrep --color=auto'
alias -g ll='ls -alF'
alias -g la='ls -A'
alias -g l='ls -CF'
alias -g mem="ps -eo pmem,pcpu,vsize,pid,cmd | sort -k 1 -nr | head -5"

# load the other files
if [ -f ~/.bocrc ]; then
  source ~/.bocrc
else
  #print "404: ~/.zsh/zshalias not found."
fi


cd ~

alias vim="nvim"
alias emustart="emulator -avd Pixel_3_XL_API_29"

# To customize prompt, run `p10k configure` or edit ~/.p10k.zsh.
[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh
alias dotfiles="/usr/bin/git --git-dir=$HOME/.dotfiles/ --work-tree=$HOME"

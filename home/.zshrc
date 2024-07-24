# Enable Powerlevel10k instant prompt. Should stay close to the top of ~/.zshrc.
# Initialization code that may require console input (password prompts, [y/n]
# confirmations, etc.) must go above this block; everything else may go below.
if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
  source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
fi

# If you come from bash you might have to change your $PATH.
export PATH=$HOME/bin:/usr/local/bin:$HOME/.local/bin:$HOME/.cargo/bin:$HOME/go/bin:$HOME/.local/share/nvim/mason/bin:$PATH
export CDPATH=$HOME/.local/share/nvim/:$CDPATH

# Path to your oh-my-zsh installation.
export ZSH="/home/jt/.oh-my-zsh"
plugins=(
    git
    zsh-autosuggestions
    zsh-syntax-highlighting
    fzf
    pipenv
)

source $ZSH/oh-my-zsh.sh


export EDITOR='nvim'

FD_OPTIONS="-a --follow --hidden --exclude .cache --exclude .git --exclude node_modules --exclude yay"
export FZF_DEFAULT_COMMAND="fd --type f --type l $FD_OPTIONS"
export FZF_CTRL_T_COMMAND="fd $FD_OPTIONS"
export FZF_ALT_C_COMMAND="fd --base-directory ~ --type d --type l $FD_OPTIONS"

alias cat="bat"
alias ll="ls -lah"

eval "$(atuin init zsh --disable-up-arrow)"
eval "$(starship init zsh)"

gch() {
 git checkout "$(git branch --all | fzf| tr -d '[:space:]')"
}

testing() {
  mkdir -p /tmp/testing
  cd /tmp/testing
  cp /home/jt/.config/nvim/minimal_init.lua /tmp/testing/min.lua
}

source ~/.secrets
ta

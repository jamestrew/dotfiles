# Enable Powerlevel10k instant prompt. Should stay close to the top of ~/.zshrc.
# Initialization code that may require console input (password prompts, [y/n]
# confirmations, etc.) must go above this block; everything else may go below.
if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
  source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
fi

# If you come from bash you might have to change your $PATH.
export PATH=$HOME/bin:/usr/local/bin:$HOME/.local/bin:$HOME/.cargo/bin:$HOME/go/src:$PATH

# Path to your oh-my-zsh installation.
export ZSH="/home/jt/.oh-my-zsh"
ZSH_THEME="powerlevel10k/powerlevel10k"
plugins=(
    git
    zsh-autosuggestions
    zsh-syntax-highlighting
    fzf
    rand-quote
    pipenv
)

source $ZSH/oh-my-zsh.sh

[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh



export EDITOR='nvim'

FD_OPTIONS="-a --follow --hidden --exclude .cache --exclude .git --exclude node_modules --exclude yay"
export FZF_DEFAULT_COMMAND="fd --type f --type l $FD_OPTIONS"
export FZF_CTRL_T_COMMAND="fd $FD_OPTIONS"
export FZF_ALT_C_COMMAND="fd --base-directory ~ --type d --type l $FD_OPTIONS"

alias py="python"
# alias ls="exa -la --icons --sort=name"
alias cat="bat"

# Perl stuff
PATH="/home/jt/perl5/bin${PATH:+:${PATH}}"; export PATH;
PERL5LIB="/home/jt/perl5/lib/perl5${PERL5LIB:+:${PERL5LIB}}"; export PERL5LIB;
PERL_LOCAL_LIB_ROOT="/home/jt/perl5${PERL_LOCAL_LIB_ROOT:+:${PERL_LOCAL_LIB_ROOT}}"; export PERL_LOCAL_LIB_ROOT;
PERL_MB_OPT="--install_base \"/home/jt/perl5\""; export PERL_MB_OPT;
PERL_MM_OPT="INSTALL_BASE=/home/jt/perl5"; export PERL_MM_OPT;

# atuin
export ATUIN_NOBIND="true"
export ATUIN_CONFIG_DIR="/home/jt/.config/atuin"
eval "$(atuin init zsh)"
bindkey '^r' _atuin_search_widget

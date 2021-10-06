#!/bin/bash
selected=`fd -a --base-directory ~/Documents -d 2 --type d | fzf`
if [[ -z $selected ]]; then
    exit 0
fi

session_name=`basename "$selected" | tr . _`
if [[ `ls $selected | grep tmux` ]]; then
    cd $selected
    worktree=`git worktree list | awk '{print $1}' | fzf`
    selected=$worktree
fi

tmux_running=`pgrep tmux`
if [[ -z $TMUX ]] && [[ -z $tmux_running ]]; then
    tmux new-session -s $session_name -c $selected
fi

if ! tmux has-session -t $session_name 2> /dev/null; then
    tmux new-session -ds $session_name -c $selected
fi

if [[ -z $TMUX ]]; then
    tmux attach-session -t $session_name
else
    tmux switch-client -t $session_name
fi


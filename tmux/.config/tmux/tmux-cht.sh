#!/bin/bash
langs=~/.config/tmux/.chtsh-langs
progs=~/.config/tmux/.chtsh-progs
selected=`cat "$langs" "$progs" | fzf`
if [[ -z $selected ]]; then
    exit 0
fi

read -p "Enter Query: " query

if grep -qs "$selected" $langs; then
    query=`echo $query | tr ' ' '+'`
    tmux neww bash -c "echo \"curl cht.sh/$selected/$query/\" & curl cht.sh/$selected/$query & while [ : ]; do sleep 1; done"
else
    tmux neww bash -c "echo \curl cht.sh/$selected~$query | less"
fi

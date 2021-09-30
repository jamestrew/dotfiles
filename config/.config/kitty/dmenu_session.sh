ls ~/.config/kitty/sessions | dmenu -i -p "Sessions:" | xargs -I {} kitty --session ~/.config/kitty/sessions/{}

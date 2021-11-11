#!/bin/sh
picom &
imwheel -b 45
clipmenud &
trayer --edge top --align right --widthtype request --padding 6 --SetDockType true --SetPartialStrut true --expand true --monitor 0 --transparent true --alpha 0 --tint 0x282c34  --height 24 &
feh --randomize --bg-fill ~/Pictures/wallpapers/*  -- feh set random wallpaper

#!/bin/sh
picom &
imwheel -b 45
clipmenud &
feh --randomize --bg-fill ~/Pictures/wallpapers/*  -- feh set random wallpaper

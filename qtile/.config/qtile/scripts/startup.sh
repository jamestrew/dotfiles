#!/bin/sh
picom &
imwheel -b 45
clipmenud &
xrandr --output DP-1 --primary --mode 3440x1440 --pos 0x480 --rotate normal --rate 144 --output DP-2 --mode 1920x1080 --pos 3440x0 --rotate left --rate 140 --output DP-3 --off --output HDMI-1 --off
feh --randomize --bg-fill ~/Pictures/wallpapers/*  -- feh set random wallpaper
teams &
discord &

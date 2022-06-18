#!/bin/sh
xrandr --output DP-1 --off --output DP-2 --mode 3440x1440 --pos 0x1080 --rotate normal --output DP-3 --off --output HDMI-1 --mode 1920x1080 --pos 760x0 --rotate normal
picom &
clipmenud &
feh --randomize --bg-fill ~/Pictures/wallpapers/*
discord &
firefox &

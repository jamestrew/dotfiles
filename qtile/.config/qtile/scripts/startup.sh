#!/bin/sh
xrandr --output DisplayPort-0 --off --output DisplayPort-1 --mode 3440x1440 --pos 0x1080 --rotate normal --output DisplayPort-2 --off --output HDMI-A-0 --mode 1920x1080 --pos 760x0 --rotate normal
picom --experimental-backends &
clipmenud &
nitrogen --restore &
discord &
firefox &

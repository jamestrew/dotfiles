#!/bin/sh

userresources=$HOME/.Xresources
usermodmap=$HOME/.Xmodmap
sysresources=/etc/X11/xinit/.Xresources
sysmodmap=/etc/X11/xinit/.Xmodmap

# merge in defaults and keymaps

if [ -f $sysresources ]; then







    xrdb -merge $sysresources

fi

if [ -f $sysmodmap ]; then
    xmodmap $sysmodmap
fi

if [ -f "$userresources" ]; then







    xrdb -merge "$userresources"

fi

if [ -f "$usermodmap" ]; then
    xmodmap "$usermodmap"
fi

# start some nice programs

if [ -d /etc/X11/xinit/xinitrc.d ] ; then
 for f in /etc/X11/xinit/xinitrc.d/?*.sh ; do
  [ -x "$f" ] && . "$f"
 done
 unset f
fi

{
  sleep 1;
  xrandr \
  --output HDMI-A-0 --mode 1920x1080 --pos 760x0 --rotate normal \
  --output DisplayPort-1 --mode 3440x1440 --pos 0x1080 --rotate normal \
  --output DisplayPort-0 --off \
  --output DisplayPort-2 --off
}
export GTK_IM_MODULE='uim'
export QT_IM_MODULE='uim'
uim-xim &
export XMODIFIERS='@im=uim'
uim-toolbar-gtk3-systray &
udiskie &
imwheel -b "45"
# exec xmonad
exec qtile start

import os
import subprocess
from typing import Optional

from libqtile import hook, qtile
from libqtile.config import Screen
from libqtile.group import _Group

import _mouse as Mouse
import _widgets as Widgets
import groups as Groups
import keys as Keys
import layouts as Layouts

keys = Keys.keys
groups = Groups.groups
layouts = Layouts.layouts
floating_layout = Layouts.floating_layout
widget_defaults = Widgets.widget_defaults
screens = [Screen(top=Widgets.main_bar), Screen(top=Widgets.sec_bar)]
mouse = Mouse.mouse
dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wmname = "LG3D"


@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser("~")
    subprocess.call([home + "/.config/qtile/startup.sh"])


@hook.subscribe.setgroup
def second_screen_wide_change():
    screens: list[Optional[Screen]] = qtile.screens
    if not screens:
        return
    if screens[0]:
        screens[0].group.cmd_setlayout("cols")
    if screens[1]:
        screens[1].group.cmd_setlayout("wide")


@hook.subscribe.group_window_add
def second_screen_wide_init(group: _Group, _):
    screen: Screen = group.screen
    if screen and screen.index == 1:
        screen.group.cmd_setlayout("wide")

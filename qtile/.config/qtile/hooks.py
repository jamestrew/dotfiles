import os
import subprocess
from typing import Optional

from libqtile import hook, qtile
from libqtile.config import Screen
from libqtile.group import _Group


@hook.subscribe.startup_once
def start_once():
    qtile = os.path.dirname(os.path.abspath(__file__))
    subprocess.call([os.path.join(qtile, "scripts/startup.sh")])


# @hook.subscribe.setgroup
# def second_screen_wide_change():
#     screens: list[Optional[Screen]] = qtile.screens
#     if not screens:
#         return
#     if screens[0]:
#         screens[0].group.cmd_setlayout("cols")
#     if screens[1]:
#         screens[1].group.cmd_setlayout("wide")
#
#
# @hook.subscribe.group_window_add
# def second_screen_wide_init(group: _Group, _):
#     screen: Screen = group.screen
#     if screen and screen.index == 1:
#         screen.group.cmd_setlayout("wide")

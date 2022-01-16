from libqtile.config import Screen

import _groups as Groups
import _keys as Keys
import _layouts as Layouts
import _mouse as Mouse
import _widgets as Widgets
import hooks

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

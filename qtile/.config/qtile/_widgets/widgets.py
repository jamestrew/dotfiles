from libqtile import bar
from libqtile.widget.base import _Widget
from libqtile.widget.clock import Clock
from libqtile.widget.currentlayout import CurrentLayout
from libqtile.widget.groupbox import GroupBox
from libqtile.widget.systray import Systray
from libqtile.widget.windowname import WindowName

from _widgets.custom_widgets import (
    audio,
    basic_sep,
    cpu,
    line_sep,
    ram,
    spotify,
    weather,
)
from colors import OneDark as c


def status_bar(widgets: list[_Widget]) -> bar.Bar:
    return bar.Bar(widgets, size=24, opacity=1)


widget_defaults = dict(
    background=c.base00,
    foreground=c.base05,
    fontsize=14,
    padding=1,
)


main_screen_widgets = [
    basic_sep,
    GroupBox(
        background=c.base00,
        active=c.base0B,
        inactive=c.base0D,
        other_current_screen_border=c.base0A,
        other_screen_border=c.base05,
        this_current_screen_border=c.base0E,
        this_screen_border=c.base05,
        urgent_border=c.base08,
        urgent_text=c.base08,
        disable_drag=True,
        highlight_method="line",
        invert_mouse_wheel=True,
        margin=2,
        padding=0,
        rounded=True,
        urgent_alert_method="text",
    ),
    line_sep,
    CurrentLayout(
        foreground=c.base0E,
    ),
    line_sep,
    WindowName(
        max_chars=75,
    ),
    *spotify,
    line_sep,
    weather,
    line_sep,
    *cpu,
    line_sep,
    *ram,
    line_sep,
    *audio,
    line_sep,
    Clock(
        foreground=c.base0C,
        format="%a %b %d  %H:%M:%S",
    ),
    Systray(
        icon_size=22,
        padding=4,
    ),
    basic_sep,
]

sec_screen_widgets = [
    basic_sep,
    GroupBox(
        background=c.base00,
        active=c.base0B,
        inactive=c.base0D,
        other_current_screen_border=c.base0A,
        other_screen_border=c.base05,
        this_current_screen_border=c.base0E,
        this_screen_border=c.base05,
        urgent_border=c.base08,
        urgent_text=c.base08,
        disable_drag=True,
        highlight_method="line",
        invert_mouse_wheel=True,
        margin=2,
        padding=0,
        rounded=True,
        urgent_alert_method="text",
    ),
    line_sep,
    CurrentLayout(
        foreground=c.base0E,
    ),
    line_sep,
    WindowName(
        max_chars=75,
    ),
    *audio,
    line_sep,
    Clock(
        foreground=c.base0C,
        format="%a %b %d  %H:%M:%S",
    ),
    Systray(
        icon_size=22,
        padding=4,
    ),
    basic_sep,
]

main_bar = status_bar(main_screen_widgets)
sec_bar = status_bar(sec_screen_widgets)

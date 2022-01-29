from libqtile import bar
from libqtile.widget.base import _Widget
from libqtile.widget.clock import Clock
from libqtile.widget.currentlayout import CurrentLayout
from libqtile.widget.pomodoro import Pomodoro
from libqtile.widget.systray import Systray
from libqtile.widget.windowname import WindowName

from _widgets.custom_widgets import (
    audio,
    basic_sep,
    cpu,
    group_box,
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
    group_box,
    line_sep,
    CurrentLayout(
        foreground=c.base0E,
    ),
    line_sep,
    WindowName(
        max_chars=75,
    ),
    Pomodoro(
        color_inactive=c.base02,
        color_active=c.base0D,
        color_break=c.base0B,
        prefix_inactive="Pomo",
        prefix_paused="Pomo - Paused ",
        prefix_break="Pomo - Break ",
        prefix_long_break="Pomo - Long Break ",
    ),
    line_sep,
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
    group_box,
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
    basic_sep,
]

main_bar = status_bar(main_screen_widgets)
sec_bar = status_bar(sec_screen_widgets)

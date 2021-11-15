from libqtile.widget.groupbox import GroupBox
from libqtile.widget.currentlayout import CurrentLayout
from libqtile.widget.currentlayout import CurrentLayout
from libqtile.widget.windowname import WindowName
from libqtile.widget.systray import Systray
from libqtile.widget.clock import Clock


from colors import OneDark as c
from widgets.custom_widgets import basic_sep, line_sep, cpu, ram, audio, weather


widget_defaults = dict(
    background=c.base00,
    foreground=c.base05,
    fontsize=14,
    padding=1,
)

extension_defaults = widget_defaults.copy()

widgets = [
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
        icon_size=14,
        padding=4,
    ),
    basic_sep,
]

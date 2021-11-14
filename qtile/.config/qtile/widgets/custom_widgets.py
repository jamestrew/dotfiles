from libqtile import qtile
from libqtile.widget.sep import Sep
from libqtile.widget.cpu import CPU
from libqtile.widget.memory import Memory
from libqtile.widget.textbox import TextBox
from libqtile.widget.clock import Clock
from libqtile.widget.pulse_volume import PulseVolume

from colors import OneDark as c

# TODO: add weather
# TODO: add spotify

basic_sep = Sep(foreground=c.base00, linewidth=4)
line_sep = Sep(foreground=c.base05, linewidth=1, padding=10)

cpu = (
    TextBox(foreground=c.base08, fontsize=22, padding=0, text=" "),
    CPU(foreground=c.base08, format="{load_percent}%", update_interval=1.0),
)

ram = (
    TextBox(foreground=c.base0B, fontsize=22, padding=0, text=" "),
    Memory(foreground=c.base0B, format="{MemPercent:.1f}%", update_interval=1.0),
)

audio = (
    TextBox(
        foreground=c.base0D,
        mouse_callbacks=(
            {
                "Button1": lambda: qtile.cmd_spawn("pamixer -t"),
                # "Button3": lambda: qtile.cmd_spawn("pavucontrol"),
                "Button4": lambda: qtile.cmd_spawn("pamixer -u -i 5"),
                "Button5": lambda: qtile.cmd_spawn("pamixer -u -d 5"),
            }
        ),
        padding=0,
        fontsize=22,
        text="墳 ",
    ),
    PulseVolume(
        foreground=c.base0D, update_interval=0.1, volume_app="pavucontrol", step=5
    ),
)

clock = (
    TextBox(
        foreground=c.base0C,
        padding=0,
        fontsize=22,
        text=" ",
    ),
    Clock(
        foreground=c.base0C,
        format="%a %b %d  %H:%M:%S",
    ),
)

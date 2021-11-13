from libqtile import qtile
from libqtile.widget.sep import Sep
from libqtile.widget.groupbox import GroupBox
from libqtile.widget.sep import Sep
from libqtile.widget.currentlayout import CurrentLayout
from libqtile.widget.cmus import Cmus
from libqtile.widget.textbox import TextBox
from libqtile.widget.currentlayout import CurrentLayout
from libqtile.widget.windowname import WindowName
from libqtile.widget.check_updates import CheckUpdates
from libqtile.widget.systray import Systray
from libqtile.widget.clock import Clock
from libqtile.widget.pulse_volume import PulseVolume

colours = [
    ["#080808", "#080808"],  # Background
    ["#FFFFFF", "#FFFFFF"],  # Foreground
    ["#ABB2BF", "#ABB2BF"],  # Grey Colour
    ["#E35374", "#E35374"],
    ["#89CA78", "#89CA78"],
    ["#F0C674", "#F0C674"],
    ["#61AFEF", "#61AFEF"],
    ["#D55FDE", "#D55FDE"],
    ["#2BBAC5", "#2BBAC5"],
]

widget_defaults = dict(
    background=colours[0],
    foreground=colours[1],
    font="SF Pro Text Regular",
    fontsize=12,
    padding=1,
)

extension_defaults = widget_defaults.copy()

widgets = [
    Sep(
        foreground=colours[0],
        linewidth=4,
    ),
    Sep(
        foreground=colours[2],
        linewidth=1,
        padding=10,
    ),
    GroupBox(
        active=colours[4],
        inactive=colours[6],
        other_current_screen_border=colours[5],
        other_screen_border=colours[2],
        this_current_screen_border=colours[7],
        this_screen_border=colours[2],
        urgent_border=colours[3],
        urgent_text=colours[3],
        disable_drag=True,
        highlight_method="text",
        invert_mouse_wheel=True,
        margin=2,
        padding=0,
        rounded=True,
        urgent_alert_method="text",
    ),
    Sep(
        foreground=colours[2],
        linewidth=1,
        padding=10,
    ),
    CurrentLayout(
        foreground=colours[7],
        font="SF Pro Text Semibold",
    ),
    Cmus(
        noplay_color=colours[2],
        play_color=colours[1],
    ),
    Sep(
        foreground=colours[2],
        linewidth=1,
        padding=10,
    ),
    WindowName(
        max_chars=75,
    ),
    TextBox(
        foreground=colours[3], font="SF Mono Regular", fontsize=14, padding=0, text=" "
    ),
    # CPU(
    # 	foreground = colours[3],
    # 	format = "{load_percent}%",
    # 	update_interval = 1.0,
    # ),
    Sep(
        foreground=colours[2],
        linewidth=1,
        padding=10,
    ),
    TextBox(
        foreground=colours[4],
        font="SF Mono Regular",
        fontsize=14,
        padding=0,
        text="﬙ ",
    ),
    # Memory(
    # 	foreground = colours[4],
    # 	format = "{MemUsed:.0f} MB",
    # 	update_interval = 1.0,
    # ),
    Sep(
        foreground=colours[2],
        linewidth=1,
        padding=10,
    ),
    # TextBox(
    # 	foreground = colours[5],
    # 	font = "SF Mono Regular",
    # 	fontsize = 12,
    # 	padding = 0,
    # 	text = " ",
    # ),
    # Backlight(
    # 	foreground = colours[5],
    # 	foreground_alert = colours[3],
    # 	backlight_name = "amdgpu_bl0", # ls /sys/class/backlight/
    # 	change_command = "brightnessctl set {0}",
    # 	step = 5,
    # ),
    TextBox(
        foreground=colours[5],
        font="SF Mono Regular",
        fontsize=14,
        padding=0,
        text=" ",
    ),
    CheckUpdates(
        colour_have_updates=colours[5],
        colour_no_updates=colours[5],
        custom_command="checkupdates",
        # 	custom_command = "dnf updateinfo -q --list",
        display_format="{updates} Updates",
        # 	execute = "pkexec /usr/bin/dnf up -y",
        execute="pkexec /usr/bin/pacman -Syu --noconfirm",
        no_update_string="Up to date!",
        update_interval=900,
    ),
    Sep(
        foreground=colours[2],
        linewidth=1,
        padding=10,
    ),
    TextBox(
        foreground=colours[6],
        font="SF Mono Regular",
        fontsize=14,
        mouse_callbacks=(
            {
                "Button1": lambda: qtile.cmd_spawn("pamixer -t"),
                "Button3": lambda: qtile.cmd_spawn("pavucontrol"),
                "Button4": lambda: qtile.cmd_spawn("pamixer -u -i 5"),
                "Button5": lambda: qtile.cmd_spawn("pamixer -u -d 5"),
            }
        ),
        padding=0,
        text="墳 ",
    ),
    PulseVolume(
        foreground=colours[6],
        update_interval=0.1,
        volume_app="pavucontrol",
        step=5,
    ),
    Sep(
        foreground=colours[2],
        linewidth=1,
        padding=10,
    ),
    TextBox(
        foreground=colours[8],
        font="SF Mono Regular",
        fontsize=14,
        padding=0,
        text=" ",
    ),
    Clock(
        foreground=colours[8],
        format="%a %b %d  %I:%M %P    ",
    ),
    Systray(
        icon_size=14,
        padding=4,
    ),
]

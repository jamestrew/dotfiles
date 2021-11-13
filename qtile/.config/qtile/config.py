import os
import subprocess
from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy

import keys as Keys

# FIX: set up binds
# TODO: set up screen
# TODO: set up start up
# TODO: set up groups
# TODO: set up bar
# TODO: set up layouts
# TODO:
# TODO:

MOD = "mod4"
SHIFT = "shift"
CTRL = "control"
TAB = "tab"


keys = Keys.keys

groups = [
    Group("www", layout="columns"),
    Group("term", layout="columns"),
    Group("sys", layout="columns"),
    Group("doc", layout="columns"),
    Group("dev", layout="columns"),
    Group(
        "work",
        layout="columns",
        matches=[
            Match(
                wm_class=[
                    "Microsoft Teams - Preview",
                ]
            )
        ],
    ),
    Group("chat", layout="columns", matches=[Match(wm_class=["discord", ""])]),
    Group("etc", layout="columns"),
    Group("oth", layout="columns", matches=[Match(wm_class=["Gimp"])]),
]

# TODO: double check this is working
for key, group in zip([1, 2, 3, 4, 5, 6, 7, 8, 9], groups):
    keys.append(EzKey(f"M-{key}", lazy.group[group.name].toscreen()))
    keys.append(EzKey(f"M-S-{key}", lazy.window.togroup(group.name)))


layout_theme = {
    "border_width": 2,
    "margin": 8,
    "border_focus": "e1acff",
    "border_normal": "1D2330",
}
layouts = [
    layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayout(),
                widget.GroupBox(),
                widget.Prompt(),
                widget.WindowName(),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.TextBox("default config", name="default"),
                widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
                widget.Systray(),
                widget.Clock(format="%Y-%m-%d %a %I:%M %p"),
                widget.QuickExit(),
            ],
            24,
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag(
        [MOD],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [MOD], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([MOD], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

wmname = "LG3D"


@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser("~")
    subprocess.call([home + "/.config/qtile/startup.sh"])

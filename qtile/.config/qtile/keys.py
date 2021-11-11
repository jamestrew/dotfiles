from libqtile.config import EzKey, Key, KeyChord
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal


MOD = "mod4"
SHIFT = "shift"
CTRL = "control"
TAB = "Tab"
SPACE = "space"

TERMINAL: str = guess_terminal("kitty")
BROWSER: str = "brave"

keys = [
    # QTILE
    EzKey("M-S-r", lazy.restart(), desc="Restart Qtile"),
    EzKey("M-S-q", lazy.shutdown(), desc="Shutdown Qtile"),
    # layouts and windows
    EzKey("M-j", lazy.layout.left(), desc="Move focus to left"),
    EzKey("M-k", lazy.layout.right(), desc="Move focus to right"),
    # EzKey([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    EzKey("M-S-j", lazy.layout.shuffle_left(), desc="Move window down"),
    EzKey("M-S-k", lazy.layout.shuffle_right(), desc="Move window up"),
    EzKey("M-h", lazy.layout.grow_left(), desc="Grow window to the left"),
    EzKey("M-l", lazy.layout.grow_right(), desc="Grow window to the right"),
    EzKey("M-<KP_Equal>", lazy.layout.normalize(), desc="Reset all window sizes"),
    EzKey("M-<space>", lazy.layout.toggle_fullscreen(), desc="fullscreen"),
    EzKey("M-<Tab>", lazy.layout.next_layout(), desc="Toggle between layouts"),
    EzKey("M-c", lazy.window.kill(), desc="Kill focused window"),
    # TODO: get all windows in group and kill each
    EzKey("M-S-c", lazy.window.kill(), desc="Kill all windows in group"),
    EzKey("M-w", lazy.layout.to_screen(0), desc="Move to screen 0"),
    EzKey("M-e", lazy.layout.to_screen(1), desc="Move to screen 1"),
    # programs
    Key([MOD], "p", lazy.spawn("dmenu_run -p 'Run: '"), desc="Run dmenu"),
    Key([MOD], "v", lazy.spawn("clipmenu"), desc="Open clipmenu"),
    Key([MOD], "v", lazy.spawn("clipmenu"), desc="Open clipmenu"),
    KeyChord(
        [MOD],
        "o",
        [
            Key([], "t", lazy.spawn(TERMINAL), desc="Open terminal"),
            Key([], "b", lazy.spawn(BROWSER), desc="Open browser"),
            Key([], "d", lazy.spawn("discord"), desc="Open discord"),
            Key([], "s", lazy.spawn("spotify"), desc="Open spotify"),
            Key([], "t", lazy.spawn(TERMINAL), desc="Open Terminal"),
        ],
    ),
    KeyChord([MOD], "s", [Key([], "s", lazy.spawn("flameshot gui"), desc="flameshot")]),
    # special keys
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer set PCM 5%+ unmute")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer set PCM 5%- unmute")),
    Key([], "XF86AudioMute", lazy.spawn("amixer set PCM toggle")),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next")),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous")),
]

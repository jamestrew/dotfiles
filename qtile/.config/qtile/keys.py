from libqtile.config import Key, KeyChord
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

# TODO: use EzKey -- http://docs.qtile.org/en/latest/manual/config/keys.html#keys

MOD = "mod4"
SHIFT = "shift"
CTRL = "control"
TAB = "tab"
SPACE = "space"

TERMINAL: str = guess_terminal("kitty")
BROWSER: str = "brave"
keys = [
    # QTILE
    Key([MOD, SHIFT], "r", lazy.restart(), desc="Restart Qtile"),
    Key([MOD, SHIFT], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    # layouts and windows
    Key([MOD], "j", lazy.layout.left(), desc="Move focus to left"),
    Key([MOD], "k", lazy.layout.right(), desc="Move focus to right"),
    # Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    Key([MOD, SHIFT], "j", lazy.layout.shuffle_left(), desc="Move window down"),
    Key([MOD, SHIFT], "k", lazy.layout.shuffle_right(), desc="Move window up"),
    Key([MOD], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([MOD], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([MOD], "=", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key([MOD], SPACE, lazy.layout.toggle_fullscreen(), desc="Toggle fullscreen"),
    Key([MOD], TAB, lazy.next_layout(), desc="Toggle between layouts"),
    Key([MOD], "c", lazy.window.kill(), desc="Kill focused window"),
    # TODO: get all windows in group and kill each
    Key([MOD, SHIFT], "c", lazy.window.kill(), desc="Kill all windows in group"),
    Key([MOD], "w", lazy.layout.to_screen(0), desc="Move to screen 0"),
    Key([MOD], "e", lazy.layout.to_screen(1), desc="Move to screen 1"),
    # programs
    Key([MOD], "p", lazy.spawn("dmenu_run -p 'Run: '"), desc="Run dmenu"),
    Key([MOD], "v", lazy.spawn("clipmenu"), desc="Open clipmenu"),
    Key([MOD], "v", lazy.spawn("clipmenu"), desc="Open clipmenu"),
    KeyChord(
        [MOD],
        "o",
        [
            Key([], "t", lazy.spawn(TERMINAL), desc="Open terminal"),
            Key([], "t", lazy.spawn(BROWSER), desc="Open browser"),
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

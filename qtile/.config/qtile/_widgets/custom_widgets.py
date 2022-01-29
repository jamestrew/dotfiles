import subprocess

from libqtile import bar, qtile
from libqtile.widget.base import InLoopPollText, _TextBox
from libqtile.widget.cpu import CPU
from libqtile.widget.groupbox import GroupBox
from libqtile.widget.memory import Memory
from libqtile.widget.open_weather import (
    OpenWeather,
    OpenWeatherResponseError,
    _OpenWeatherResponseParser,
)
from libqtile.widget.pulse_volume import PulseVolume
from libqtile.widget.sep import Sep

from colors import OneDark as c

__all__ = [
    "group_box",
    "spotify",
    "weather",
    "line_sep",
    "basic_sep",
    "cpu",
    "ram",
    "audio",
]


class Icon(_TextBox):
    def __init__(self, text=" ", width=bar.CALCULATED, **config):
        super().__init__(text=text, width=width, **config)
        self.fmt = "{} "
        self.fontsize = 22
        self.padding = 0
        # TODO: add vertical padding?


class CustomWeather(OpenWeather):
    symbols = {
        "Unknown": "",
        "01d": " ",
        "01n": " ",
        "02d": " ",
        "02n": " ",
        "03d": " ",
        "03n": " ",
        "04d": " ",
        "04n": " ",
        "09d": " ",
        "09n": " ",
        "10d": " ",
        "10n": " ",
        "11d": " ",
        "11n": " ",
        "13d": "禮",
        "13n": "禮",
        "50d": " ",
        "50n": " ",
    }

    def __init__(self, **config):
        super().__init__(**config)
        self.format = "{icon} {main_feels_like:.0f}糖 {humidity} {wind_speed:.0f} "

    def parse(self, response):
        try:
            rp = _OpenWeatherResponseParser(response, self.dateformat, self.timeformat)
        except OpenWeatherResponseError as e:
            return "Error {}".format(e.resp_code)

        data = rp.data
        data["units_temperature"] = "C" if self.metric else "F"
        data["units_wind_speed"] = "Km/h" if self.metric else "m/h"
        data["icon"] = self.symbols.get(data["weather_0_icon"], self.symbols["Unknown"])

        return self.format.format(**data)


class Spotify(InLoopPollText):
    def __init__(self, default_text="N/A", width=bar.CALCULATED, **config):
        super().__init__(default_text=default_text, width=width, **config)
        self.update_interval = 3
        self.add_callbacks(
            {"Button1": lambda: qtile.cmd_spawn("playerctl -p spotify play-pause")}
        )

    def poll(self):
        script_dir = "/home/jt/.config/qtile/scripts/music.sh"
        out = subprocess.run([script_dir, "/dev/null"], capture_output=True)
        return out.stdout.decode("utf-8").strip() or "N/A"


basic_sep = Sep(foreground=c.base00, linewidth=4)
line_sep = Sep(foreground=c.base05, linewidth=1, padding=10)

group_box = GroupBox(
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
)

cpu = (
    Icon(foreground=c.base08, text=""),
    CPU(foreground=c.base08, format="{load_percent: >4}%", update_interval=1.0),
)

ram = (
    Icon(foreground=c.base0B, text=""),
    Memory(foreground=c.base0B, format="{MemPercent: >4.1f}%", update_interval=1.0),
)

audio = (
    Icon(
        foreground=c.base0D,
        mouse_callbacks={
            "Button1": lambda: qtile.cmd_spawn("amixer set PCM toggle"),
            "Button3": lambda: qtile.cmd_spawn("pavucontrol"),
            "Button4": lambda: qtile.cmd_spawn("amixer set PCM 1%+ unmute"),
            "Button5": lambda: qtile.cmd_spawn("amixer set PCM 1%- unmute"),
        },
        text="墳",
    ),
    PulseVolume(
        foreground=c.base0D, update_interval=0.1, volume_app="pavucontrol", step=1
    ),
)

spotify = (Icon(foreground=c.base08, text="阮"), Spotify(foreground=c.base08))

weather = CustomWeather(
    cityid=6167865,
    fontsize=16,
    foreground=c.base0E,
)

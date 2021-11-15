from libqtile import qtile
from libqtile.widget.sep import Sep
from libqtile.widget.cpu import CPU
from libqtile.widget.memory import Memory
from libqtile.widget.textbox import TextBox
from libqtile.widget.pulse_volume import PulseVolume
from libqtile.widget.open_weather import (
    OpenWeather,
    OpenWeatherResponseError,
    _OpenWeatherResponseParser,
)

from colors import OneDark as c

# TODO: add spotify


class Icon(_TextBox):
    def __init__(self, **config):
        super().__init__(**config)
        self.fmt = "{} "
        self.fontsize = 22
        self.padding = 0
        # TODO: add vertical padding?

class CustomWeather(OpenWeather):
    symbols = {
        "Unknown": "✨",
        "01d": "☀️",
        "01n": "🌕",
        "02d": "🌤️",
        "02n": "☁️",
        "03d": "🌥️",
        "03n": "☁️",
        "04d": "☁️",
        "04n": "☁️",
        "09d": "🌧️",
        "09n": "🌧️",
        "10d": "⛈",
        "10n": "⛈",
        "11d": "🌩",
        "11n": "🌩",
        "13d": "❄️",
        "13n": "❄️",
        "50d": "🌫",
        "50n": "🌫",
    }

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


basic_sep = Sep(foreground=c.base00, linewidth=4)
line_sep = Sep(foreground=c.base05, linewidth=1, padding=10)

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
        mouse_callbacks=(
            {
                "Button1": lambda: qtile.cmd_spawn("pamixer -t"),
                # "Button3": lambda: qtile.cmd_spawn("pavucontrol"),
                "Button4": lambda: qtile.cmd_spawn("pamixer -u -i 5"),
                "Button5": lambda: qtile.cmd_spawn("pamixer -u -d 5"),
            }
        ),
        text="墳",
    ),
    PulseVolume(
        foreground=c.base0D, update_interval=0.1, volume_app="pavucontrol", step=5
    ),
)

weather = CustomWeather(
    cityid=6167865,
    format="{icon} {main_feels_like:.0f}糖 {humidity} {wind_speed:.0f} ",
    fontsize=16,
    foreground=c.base0E
)

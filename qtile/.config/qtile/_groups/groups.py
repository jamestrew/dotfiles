from libqtile.config import Group, Match

group_bindings = [1, 2, 3, 4, 5]
groups = [
    Group("www", layout="cols"),
    Group("sys", layout="cols"),
    Group("coms", layout="cols", matches=[Match(wm_class=["discord", ""])]),
    Group("doc", layout="cols"),
    Group("dev", layout="cols"),
]

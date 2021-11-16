from libqtile.config import Group, Match

group_bindings = [1, 2, 3, 4, 5, 6, 7, 8, 9]
groups = [
    Group("www", layout="cols"),
    Group("term", layout="cols"),
    Group("sys", layout="cols"),
    Group("doc", layout="cols"),
    Group("dev", layout="cols"),
    Group(
        "work",
        layout="cols",
        matches=[
            Match(
                wm_class=[
                    "Microsoft Teams - Preview",
                ]
            )
        ],
    ),
    Group("chat", layout="cols", matches=[Match(wm_class=["discord", ""])]),
    Group("etc", layout="cols"),
    Group("oth", layout="cols", matches=[Match(wm_class=["Gimp"])]),
]

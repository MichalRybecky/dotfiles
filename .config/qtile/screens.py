import os
import subprocess

from libqtile.config import (
    # KeyChord,
    # Key,
    Screen,
    # Group,
    # Drag,
    # Click,
    # ScratchPad,
    # DropDown,
    # Match,
)
# from libqtile.command import lazy
from libqtile import bar, widget # , hook, layout
# from libqtile.lazy import lazy
from libqtile import qtile
# from custom.bsp import Bsp as CustomBsp
# from custom.zoomy import Zoomy as CustomZoomy
# from custom.stack import Stack as CustomStack
from custom.windowname import WindowName as CustomWindowName

from colors import colors

terminal = "alacritty"


def bluetooth():
    return (
        subprocess.check_output(["./.config/qtile/system-bluetooth-bluetoothctl.sh"])
        .decode("utf-8")
        .strip()
    )


def update():
    qtile.cmd_spawn(terminal + "-e yay")


def open_bt_menu():
    qtile.cmd_spawn("blueman")


def open_pavu():
    qtile.cmd_spawn("pavucontrol")


def toggle_bluetooth():
    qtile.cmd_spawn("./.config/qtile/system-bluetooth-bluetoothctl.sh --toggle")


def taskwarrior():
    return (
        subprocess.check_output(["./.config/qtile/task_polybar.sh"])
        .decode("utf-8")
        .strip()
    )


group_box_settings = {
    "padding": 5,
    "borderwidth": 4,
    "active": colors[9],
    "inactive": colors[10],
    "disable_drag": True,
    "rounded": True,
    "highlight_color": colors[2],
    "block_highlight_text_color": colors[6],
    "highlight_method": "block",
    "this_current_screen_border": colors[14],
    "this_screen_border": colors[7],
    "other_current_screen_border": colors[14],
    "other_screen_border": colors[14],
    "foreground": colors[1],
    "background": colors[14],
    "urgent_border": colors[3],
}


screens = [
    Screen(
        wallpaper="~/Pictures/snowy-mountains.jpg",
        wallpaper_mode="fill",
        top=bar.Bar(
            [
                widget.TextBox(
                    text="",
                    foreground=colors[13],
                    background=colors[0],
                    fontsize=28,
                    padding=20,
                ),
                widget.TextBox(
                    text="",
                    foreground=colors[14],
                    background=colors[0],
                    fontsize=28,
                    padding=0,
                ),
                widget.GroupBox(
                    font="Font Awesome 5 Brands",
                    visible_groups=[""],
                    **group_box_settings,
                ),
                widget.GroupBox(
                    font="Font Awesome 5 Free Solid",
                    visible_groups=["", "", "", ""],
                    **group_box_settings,
                ),
                widget.GroupBox(
                    font="Font Awesome 5 Brands",
                    visible_groups=[""],
                    **group_box_settings,
                ),
                widget.GroupBox(
                    font="Font Awesome 5 Free Solid",
                    visible_groups=[""],
                    **group_box_settings,
                ),
                widget.GroupBox(
                    font="Font Awesome 5 Brands",
                    visible_groups=[""],
                    **group_box_settings,
                ),

                widget.TextBox(
                    text="",
                    foreground=colors[14],
                    background=colors[0],
                    fontsize=28,
                    padding=0,
                ),
                widget.Sep(
                    linewidth=0,
                    foreground=colors[2],
                    background=colors[0],
                    padding=10,
                    size_percent=40,
                ),
                # widget.TextBox(
                #    text=" ",
                #    foreground=colors[7],
                #    background=colors[0],
                #    font="Font Awesome 5 Free Solid",
                # ),
                # widget.CurrentLayout(
                #    background=colors[0],
                #    foreground=colors[7],
                # ),
                widget.TextBox(
                    text="",
                    foreground=colors[14],
                    background=colors[0],
                    fontsize=28,
                    padding=0,
                ),
                widget.CurrentLayoutIcon(
                    custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons")],
                    foreground=colors[2],
                    background=colors[14],
                    padding=-2,
                    scale=0.45,
                ),
                widget.TextBox(
                    text="",
                    foreground=colors[14],
                    background=colors[0],
                    fontsize=28,
                    padding=0,
                ),
                widget.Sep(
                    linewidth=0,
                    foreground=colors[2],
                    padding=10,
                    size_percent=50,
                ),
                widget.TextBox(
                    text="",
                    foreground=colors[14],
                    background=colors[0],
                    fontsize=28,
                    padding=0,
                ),
                widget.GenPollText(
                    func=taskwarrior,
                    update_interval=20,
                    foreground=colors[11],
                    background=colors[14],
                ),
                widget.TextBox(
                    text="",
                    foreground=colors[14],
                    background=colors[0],
                    fontsize=28,
                    padding=0,
                ),
                widget.Spacer(),
                widget.TextBox(
                    text=" ",
                    foreground=colors[12],
                    background=colors[0],
                    font="Font Awesome 5 Free Solid",
                ),
                CustomWindowName(
                    background=colors[0],
                    foreground=colors[12],
                    width=bar.CALCULATED,
                    empty_group_string="Desktop",
                    max_chars=60,
                ),
                widget.CheckUpdates(
                    background=colors[0],
                    foreground=colors[3],
                    colour_have_updates=colors[3],
                    display_format=" {updates}",
                    execute=update,
                    padding=20,
                    update_interval=300,
                ),
                widget.Spacer(),
                # widget.TextBox(
                #     text="",
                #     foreground=colors[14],
                #     background=colors[0],
                #     fontsize=28,
                #     padding=0,
                # ),
                widget.Systray(background=colors[0], padding=20),
                # widget.TextBox(
                #     text="",
                #     foreground=colors[14],
                #     background=colors[0],
                #     fontsize=28,
                #     padding=0,
                # ),
                widget.Sep(
                    linewidth=0,
                    foreground=colors[2],
                    padding=10,
                    size_percent=50,
                ),
                widget.TextBox(
                    text="",
                    foreground=colors[14],
                    background=colors[0],
                    fontsize=28,
                    padding=0,
                ),
                widget.TextBox(
                    text=" ",
                    foreground=colors[8],
                    background=colors[14],
                    font="Font Awesome 5 Free Solid",
                    # fontsize=38,
                ),
                widget.PulseVolume(
                    foreground=colors[8],
                    background=colors[14],
                    limit_max_volume="True",
                    update_interval=0.1,
                    mouse_callbacks={"Button3": open_pavu},
                ),
                widget.TextBox(
                    text="",
                    foreground=colors[14],
                    background=colors[0],
                    fontsize=28,
                    padding=0,
                ),
                widget.Sep(
                    linewidth=0,
                    foreground=colors[2],
                    padding=10,
                    size_percent=50,
                ),
                widget.TextBox(
                    text="",
                    foreground=colors[14],
                    background=colors[0],
                    fontsize=28,
                    padding=0,
                ),
                # widget.GenPollText(
                #     func=bluetooth,
                #     background=colors[14],
                #     foreground=colors[6],
                #     update_interval=3,
                #     mouse_callbacks={
                #         "Button1": toggle_bluetooth,
                #         "Button3": open_bt_menu,
                #     },
                # ),
                widget.TextBox(
                    text="",
                    font="Font Awesome 5 Free Solid",
                    foreground=colors[6],  # fontsize=38
                    background=colors[14],
                ),
                widget.CPU(
                    background=colors[14],
                    foreground=colors[6],
                    update_interval=1,
                    format="{load_percent: .0f} %",
                ),
                widget.TextBox(
                    text="",
                    foreground=colors[14],
                    background=colors[0],
                    fontsize=28,
                    padding=0,
                ),
                widget.Sep(
                    linewidth=0,
                    foreground=colors[2],
                    padding=10,
                    size_percent=50,
                ),
                widget.TextBox(
                    text="",
                    foreground=colors[14],
                    background=colors[0],
                    fontsize=28,
                    padding=0,
                ),
                widget.TextBox(
                    text="",
                    font="Font Awesome 5 Free Solid",
                    foreground=colors[7],  # fontsize=38
                    background=colors[14],
                ),
                widget.Memory(
                    foreground=colors[7],
                    background=colors[14],
                    format="{MemPercent: .0f} %"
                ),
                # 
                # widget.Wlan(
                #     interface="enp4s0",
                #     format="{quality}",
                #     foreground=colors[7],
                #     background=colors[14],
                #     padding=5,
                # ),
                widget.TextBox(
                    text="",
                    foreground=colors[14],
                    background=colors[0],
                    fontsize=28,
                    padding=0,
                ),
                widget.Sep(
                    linewidth=0,
                    foreground=colors[2],
                    padding=10,
                    size_percent=50,
                ),
                widget.TextBox(
                    text="",
                    foreground=colors[14],
                    background=colors[0],
                    fontsize=28,
                    padding=0,
                ),
                widget.TextBox(
                    text=" ",
                    font="Font Awesome 5 Free Solid",
                    foreground=colors[5],  # fontsize=38
                    background=colors[14],
                ),
                widget.Clock(
                    format="%b %d",
                    background=colors[14],
                    foreground=colors[5],
                ),
                widget.TextBox(
                    text="",
                    foreground=colors[14],
                    background=colors[0],
                    fontsize=28,
                    padding=0,
                ),
                widget.Sep(
                    linewidth=0,
                    foreground=colors[2],
                    padding=10,
                    size_percent=50,
                ),
                widget.TextBox(
                    text="",
                    foreground=colors[14],
                    background=colors[0],
                    fontsize=28,
                    padding=0,
                ),
                widget.TextBox(
                    text=" ",
                    font="Font Awesome 5 Free Solid",
                    foreground=colors[4],  # fontsize=38
                    background=colors[14],
                ),
                widget.Clock(
                    format="%H:%M",
                    foreground=colors[4],
                    background=colors[14],
                ),
                widget.TextBox(
                    text="",
                    foreground=colors[14],
                    background=colors[0],
                    fontsize=28,
                    padding=0,
                ),
                widget.Sep(
                   linewidth=0,
                   foreground=colors[2],
                   padding=10,
                   size_percent=50,
                ),
            ],
            38,
            margin=[0, -4, 10, -4],
        ),
        bottom=bar.Gap(5),
        left=bar.Gap(5),
        right=bar.Gap(5),
    ),
]

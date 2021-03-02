# -*- coding: utf-8 -*-
import os
import re
import socket
import subprocess
import psutil

from colors import colors
from screens import screens

from libqtile.config import (
    KeyChord,
    Key,
    Screen,
    Group,
    Drag,
    Click,
    ScratchPad,
    DropDown,
    Match,
)
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
from libqtile.lazy import lazy
from libqtile import qtile
from typing import List  # noqa: F401
from custom.bsp import Bsp as CustomBsp
from custom.zoomy import Zoomy as CustomZoomy
from custom.stack import Stack as CustomStack
from custom.windowname import WindowName as CustomWindowName

mod = "mod4"
terminal = "urxvt"
myconfig = "/home/michal/.config/qtile/config.py"

## Resize functions for bsp layout
def resize(qtile, direction):
    layout = qtile.current_layout
    child = layout.current
    parent = child.parent

    while parent:
        if child in parent.children:
            layout_all = False

            if (direction == "left" and parent.split_horizontal) or (
                direction == "up" and not parent.split_horizontal
            ):
                parent.split_ratio = max(5, parent.split_ratio - layout.grow_amount)
                layout_all = True
            elif (direction == "right" and parent.split_horizontal) or (
                direction == "down" and not parent.split_horizontal
            ):
                parent.split_ratio = min(95, parent.split_ratio + layout.grow_amount)
                layout_all = True

            if layout_all:
                layout.group.layout_all()
                break

        child = parent
        parent = child.parent


@lazy.function
def resize_left(qtile):
    resize(qtile, "left")


@lazy.function
def resize_right(qtile):
    resize(qtile, "right")


@lazy.function
def resize_up(qtile):
    resize(qtile, "up")


@lazy.function
def resize_down(qtile):
    resize(qtile, "down")


keys = [
    ### The essentials
    Key([mod], "Return", lazy.spawn(terminal), desc="Launches My Terminal"),
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle through layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill active window"),
    Key([mod, "shift"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "shift"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod, "shift"], "a", lazy.spawn("subl /home/michal/.config/qtile/config.py"), desc="Config qtile",),
    Key([mod], "w", lazy.spawn("librewolf"), desc="Launches LibreWolf"),
    Key([mod], "d", lazy.spawn("dmenu_run"), desc="Launches dmenu"),

    ### Window controls
    Key(
        [mod], "j", lazy.layout.down(), desc="Move focus down in current stack pane"
    ),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up in current stack pane"),
    Key(
        [mod],
        "h",
        lazy.layout.left(),
        lazy.layout.next(),
        desc="Move focus left in current stack pane",
    ),
    Key(
        [mod],
        "l",
        lazy.layout.right(),
        lazy.layout.previous(),
        desc="Move focus right in current stack pane",
    ),
    Key(
        [mod, "shift"],
        "j",
        lazy.layout.shuffle_down(),
        desc="Move windows down in current stack",
    ),
    Key(
        [mod, "shift"],
        "k",
        lazy.layout.shuffle_up(),
        desc="Move windows up in current stack",
    ),
    Key(
        [mod, "shift"],
        "h",
        lazy.layout.shuffle_left(),
        lazy.layout.swap_left(),
        lazy.layout.client_to_previous(),
        desc="Move windows left in current stack",
    ),
    Key(
        [mod, "shift"],
        "l",
        lazy.layout.shuffle_right(),
        lazy.layout.swap_right(),
        lazy.layout.client_to_next(),
        desc="Move windows right in the current stack",
    ),
    Key([mod, "control"], "j", lazy.layout.flip_down(), desc="Flip layout down"),
    Key([mod, "control"], "k", lazy.layout.flip_up(), desc="Flip layout up"),
    Key([mod, "control"], "h", lazy.layout.flip_left(), desc="Flip layout left"),
    Key([mod, "control"], "l", lazy.layout.flip_right(), desc="Flip layout right"),
    Key([mod], "u", resize_left, desc="Resize window left",),
    Key([mod], "i", resize_right, desc="Resize window Right",),
    Key([mod], "o", resize_up, desc="Resize windows upward"),
    Key([mod], "p", resize_down, desc="Resize windows downward"),
    Key([mod], "n", lazy.layout.normalize(), desc="Normalize window size ratios"),
    Key([mod], "m", lazy.layout.maximize(),
    	desc="Toggle window between minimum and maximum sizes",
    ),
    Key([mod, "shift"], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen"),
    Key([mod], "equal", lazy.layout.grow(), desc="Grow in monad tall"),
    Key([mod], "minus", lazy.layout.shrink(), desc="Shrink in monad tall"),
    Key(
        [mod],
        "t",
        lazy.window.toggle_floating(),
        desc="Toggle floating on focused window",
    ),
    ### Stack controls
    Key(
        [mod],
        "f",
        lazy.layout.rotate(),
        lazy.layout.flip(),
        desc="Switch which side main pane occupies {MonadTall}",
    ),
    # Key(
    #    [mod],
    #    "f",
    #    lazy.layout.next(),
    #    desc="Switch window focus to other pane/s of stack",
    # ),
    Key(
        [mod],
        "s",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    ### Misc. Commands
    Key(
        [mod],
        "b",
        lazy.spawn("qtile-cmd -o cmd -f hide_show_bar"),
        desc="Toggle bar visibility",
    ),
    Key(
        [mod],
        "backslash",
        lazy.spawn("sh -c 'thunar \"$(xcwd)\"'"),
        desc="Launch thunar",
    ),
    Key(
        [mod, "shift"],
        "Return",
        lazy.spawn("sh -c 'alacritty --working-directory \"$(xcwd)\"'"),
        desc="Launch terminal from directory of focused window",
    ),
    Key(
        [mod, "mod1"],
        "space",
        lazy.spawn("./.config/sxhkd/old_scripts/rofi-task"),
        desc="Rofi taskwarrior",
    ),
    Key([mod, "shift"], "m", lazy.spawn("splatmoji copy"), desc="*moji selector"),
    Key(
        [mod, "shift"],
        "w",
        lazy.spawn("./.config/qtile/focus_mode.sh"),
        desc="Toggle focus mode",
    ),
    Key(
        [mod, "control"],
        "w",
        lazy.spawn("rofi -theme ~/.config/rofi/configTall.rasi -show window"),
        # lazy.spawn("rofi -display-window '□' -show window"),
        desc="Rofi window select",
    ),
    Key(
        [mod, "control"],
        "w",
        lazy.spawn("nc_flash_window"),
        desc="Flash currently focused window",
    ),
    Key(
        [mod],
        "space",
        lazy.spawn("./.config/sxhkd/old_scripts/rofi_notes.sh"),
        desc="Rofi quick notes",
    ),
    Key(
        [],
        "Print",
        lazy.spawn("./.config/sxhkd/prtscr"),
        desc="Print Screen",
    ),
    Key(
        [mod],
        "Print",
        lazy.spawn("./.config/sxhkd/prtregion -d"),
        desc="Print region of screen",
    ),
    Key(
        [mod, "shift"],
        "Print",
        lazy.spawn("./.config/sxhkd/prtregion -c"),
        desc="Print region of screen to clipboard",
    ),
    # Key(
    #    [mod],
    #    "F10",
    #    lazy.spawn("./.config/qtile/eww_bright.sh up"),
    #    desc="Increase brightness",
    # ),
    # Key(
    #    [mod],
    #    "F9",
    #    lazy.spawn("./.config/qtile/eww_bright.sh down"),
    #    desc="Decrease brightness",
    # ),
    Key(
        [],
        "XF86AudioRaiseVolume",
        lazy.spawn("./.config/qtile/eww_vol.sh up"),
        desc="Increase volume",
    ),
    Key(
        [],
        "XF86AudioLowerVolume",
        lazy.spawn("./.config/qtile/eww_vol.sh down"),
        desc="Decrease volume",
    ),
    Key(
        [],
        "XF86AudioMute",
        lazy.spawn("./.config/qtile/eww_vol.sh mute"),
        desc="Toggle mute",
    ),
    Key(
        [mod],
        "XF86AudioRaiseVolume",
        lazy.spawn("./.config/sxhkd/vol pulsemic up"),
        desc="Increase mic volume",
    ),
    Key(
        [mod],
        "XF86AudioLowerVolume",
        lazy.spawn("./.config/sxhkd/vol pulsemic down"),
        desc="Decrease mic volume",
    ),
    Key(
        [mod],
        "XF86AudioMute",
        lazy.spawn("./.config/sxhkd/vol pulsemic mute"),
        desc="Toggle mic mute",
    ),
    Key(
        [mod],
        "F7",
        lazy.spawn("playerctl previous"),
        desc="Play last audio",
    ),
    Key([mod], "F8", lazy.spawn("playerctl next"), desc="Play next audio"),
    Key(
        [mod], "F5", lazy.spawn("playerctl play-pause"), desc="Toggle play/pause audio"
    ),
    Key([mod], "F6", lazy.spawn("playerctl stop"), desc="Stop audio"),
    Key(
        [mod], "F4", lazy.spawn("./.config/sxhkd/.caffeine.sh"), desc="Toggle caffeine"
    ),
    Key(
        [mod],
        "z",
        lazy.spawn("./.config/sxhkd/old_scripts/rofi-files"),
        desc="Find files",
    ),
    Key(
        [mod, "shift"],
        "z",
        lazy.spawn("./.config/sxhkd/rofi-search.sh"),
        desc="Google search",
    ),
    Key(
        [mod, "control"],
        "r",
        lazy.spawn("mp4"),
        desc="Record selected part of screen in mp4",
    ),
    Key(
        [mod, "control", "shift"],
        "r",
        lazy.spawn("gif"),
        desc="Record selected part of screen as gif",
    ),
    Key(
        [mod, "shift"],
        "p",
        lazy.spawn("./.config/sxhkd/togglepicom"),
        desc="Toggle picom",
    ),
    Key([mod], "x", lazy.spawn("./.config/sxhkd/greenclip"), desc="Greenclip"),
    Key([mod, "shift"], "c", lazy.spawn("colorpick.sh"), desc="Color picker"),
    Key([mod], "j", lazy.spawn("./.config/sxhkd/spotnotif"), desc="What is playing?"),
    Key(
        [mod, "control"],
        "c",
        lazy.spawn("./.config/sxhkd/old_scripts/toggledunst"),
        desc="Toggle dunst",
    ),
    Key(
        [mod, "mod1"],
        "c",
        lazy.spawn(
            "sh -c 'xdotool mousemove --window \"$(xdotool getwindowfocus)\" --polar 0 0'"
        ),
        desc="Teleport cursor to center of focused window",
    ),
    Key(
        [mod],
        "grave",
        lazy.spawn("./.local/bin/rofi_notif_center.sh"),
        desc="Open notification center",
    ),
    Key(
        [],
        "XF86Calculator",
        lazy.spawn("galculator"),
        desc="Launch calculator",
    ),
    Key(
        [mod],
        "r",
        lazy.spawn("./.config/qtile/toggle_redshift.sh"),
        desc="Toggle redshift",
    ),
]


def show_keys():
    key_help = ""
    for k in keys:
        mods = ""

        for m in k.modifiers:
            if m == "mod4":
                mods += "Super + "
            else:
                mods += m.capitalize() + " + "

        if len(k.key) > 1:
            mods += k.key.capitalize()
        else:
            mods += k.key

        key_help += "{:<30} {}".format(mods, k.desc + "\n")

    return key_help


keys.extend(
    [
        Key(
            [mod],
            "a",
            lazy.spawn(
                "sh -c 'echo \""
                + show_keys()
                + '" | rofi -dmenu -theme ~/.config/rofi/configTall.rasi -i -p "?"\''
            ),
            desc="Print keyboard bindings",
        ),
    ]
)

workspaces = [
    {"name": "", "key": "1", "matches": [
        Match(wm_class="librewolf"),
        Match(wm_class="firefox"),
        Match(wm_class="firefox-nightly"),
        ]},
    {
        "name": "",
        "key": "2",
        "matches": [Match(wm_class="signal-desktop")],
    },
    {
        "name": "",
        "key": "3",
        "matches": [
            Match(wm_class="joplin"),
            Match(wm_class="libreoffice"),
            Match(wm_class="org.pwmt.zathura"),
        ],
    },
    {"name": "", "key": "4", "matches": [Match(wm_class="subl")]},
    {"name": "", "key": "5", "matches": [Match(wm_class="")]},
    {
        "name": "",
        "key": "6",
        "matches": [
            Match(wm_class="slack"),
            Match(wm_class="lightcord"),
            Match(wm_class="polari"),
        ],
    },
    {"name": "", "key": "7", "matches": [Match(wm_class="spotify")]},
    {"name": "", "key": "8", "matches": [Match(wm_class="teams-for-linux")]},
    {"name": "", "key": "9", "matches": [Match(wm_class="virtualbox")]},
    {
        "name": "",
        "key": "0",
        "matches": [
            Match(wm_class="lxappearance"),
            Match(wm_class="pavucontrol"),
            Match(wm_class="connman-gtk"),
        ],
    },
]

groups = []
#     ScratchPad(
#         "scratchpad",
#         [
#             # define a drop down terminal.
#             # it is placed in the upper third of screen by default.
#             DropDown(
#                 "term",
#                 "alacritty --class dropdown -e tmux_startup.sh",
#                 height=0.6,
#                 on_focus_lost_hide=False,
#                 opacity=1,
#                 warp_pointer=False,
#             ),
#             DropDown(
#                 "fm",
#                 "thunar",
#                 width=0.6,
#                 height=0.6,
#                 x=0.2,
#                 y=0.1,
#                 on_focus_lost_hide=False,
#                 opacity=1,
#                 warp_pointer=True,
#             ),
#         ],
#     ),
# ]

for workspace in workspaces:
    matches = workspace["matches"] if "matches" in workspace else None
    groups.append(Group(workspace["name"], matches=matches, layout="bsp"))
    keys.append(
        Key(
            [mod],
            workspace["key"],
            lazy.group[workspace["name"]].toscreen(),
            desc="Focus this desktop",
        )
    )
    keys.append(
        Key(
            [mod, "shift"],
            workspace["key"],
            lazy.window.togroup(workspace["name"]),
            desc="Move focused window to another group",
        )
    )

layout_theme = {
    "border_width": 3,
    "margin": 7,
    "border_focus": "3b4252",
    "border_normal": "3b4252",
    "font": "FiraCode Nerd Font",
    "grow_amount": 2,
}

layouts = [
    # layout.MonadWide(**layout_theme),
    # layout.Bsp(**layout_theme, fair=False, grow_amount=2),
    CustomBsp(**layout_theme, fair=False),
    # layout.Columns(
    #    **layout_theme,
    #    border_on_single=True,
    #    num_columns=3,
    #    # border_focus_stack=colors[2],
    #    # border_normal_stack=colors[2],
    #    split=False,
    # ),
    layout.RatioTile(**layout_theme),
    # layout.VerticalTile(**layout_theme),
    # layout.Matrix(**layout_theme, columns=3),
    CustomZoomy(**layout_theme),
    # layout.Slice(**layout_theme),
    # layout.TreeTab(
    #    **layout_theme,
    #    active_bg=colors[14],
    #    active_fg=colors[1],
    #    bg_color=colors[0],
    #    fontsize=16,
    #    inactive_bg=colors[0],
    #    inactive_fg=colors[1],
    #    sections=["TreeTab", "TreeTab2"],
    #    section_fontsize=18,
    #    section_fg=colors[1],
    # ),
    # layout.MonadTall(**layout_theme),
    # layout.Max(**layout_theme),
    # layout.Tile(shift_windows=True, **layout_theme),
    # layout.Floating(**layout_theme, fullscreen_border_width=3, max_border_width=3),
]

# Setup bar

widget_defaults = dict(
    font="FiraCode Nerd Font", fontsize=18, padding=3, background=colors[0]
)
extension_defaults = widget_defaults.copy()


### Mouse_callback functions

def kill_window():
    qtile.cmd_spawn("xdotool getwindowfocus windowkill")


def open_connman():
    qtile.cmd_spawn("connman-gtk")


# Drag floating layouts.
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = "floating_only"
cursor_warp = False
floating_layout = layout.Floating(
    **layout_theme,
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        Match(wm_type="utility"),
        Match(wm_type="notification"),
        Match(wm_type="toolbar"),
        Match(wm_type="splash"),
        Match(wm_type="dialog"),
        Match(wm_class="confirm"),
        Match(wm_class="dialog"),
        Match(wm_class="download"),
        Match(wm_class="error"),
        Match(wm_class="file_progress"),
        Match(wm_class="notification"),
        Match(wm_class="splash"),
        Match(wm_class="toolbar"),
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(wm_class="pomotroid"),
        Match(wm_class="cmatrixterm"),
        Match(title="Farge"),
        Match(wm_class="thunar"),
        Match(wm_class="feh"),
        Match(wm_class="galculator"),
        Match(wm_class="blueman-manager"),
    ],
)
auto_fullscreen = True
focus_on_window_activation = "focus"

# Startup scripts
@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser("~")
    subprocess.call([home + "/.config/qtile/autostart.sh"])


# Window swallowing ;)
@hook.subscribe.client_new
def _swallow(window):
    pid = window.window.get_net_wm_pid()
    ppid = psutil.Process(pid).ppid()
    cpids = {
        c.window.get_net_wm_pid(): wid for wid, c in window.qtile.windows_map.items()
    }
    for i in range(5):
        if not ppid:
            return
        if ppid in cpids:
            parent = window.qtile.windows_map.get(cpids[ppid])
            parent.minimized = True
            window.parent = parent
            return
        ppid = psutil.Process(ppid).ppid()


@hook.subscribe.client_killed
def _unswallow(window):
    if hasattr(window, "parent"):
        window.parent.minimized = False


# Go to group when app opens on matched group
@hook.subscribe.client_new
def modify_window(client):
    # if (client.window.get_wm_transient_for() or client.window.get_wm_type() in floating_types):
    #    client.floating = True

    for group in groups:  # follow on auto-move
        match = next((m for m in group.matches if m.compare(client)), None)
        if match:
            targetgroup = client.qtile.groups_map[
                group.name
            ]  # there can be multiple instances of a group
            targetgroup.cmd_toscreen(toggle=False)
            break


# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

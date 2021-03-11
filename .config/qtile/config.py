import os
import re
import socket
import subprocess
from libqtile.config import Drag, Key, Screen, Match, Group, Drag, Click, Rule
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
from libqtile.widget import Spacer

from custom.windowname import WindowName as CustomWindowName
#mod4 or mod = super key
mod = "mod4"
mod1 = "alt"
mod2 = "control"
home = os.path.expanduser('~')
myTerminal = "kitty"
# focus_on_window_activation = "never"


@lazy.function
def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)

@lazy.function
def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)

keys = [

# essentials

    Key([], "F12", lazy.spawn('xfce4-terminal --drop-down')),

    Key([mod], "Return",
        lazy.spawn(myTerminal),
        desc= "Run Terminal"
        ),
    Key([mod, "shift"], "Return",
        lazy.spawn("rofi -theme ~/.config/rofi/nord.rasi -show drun"),
        desc= "Run Launcher"
        ),
    Key([mod, "shift"], "d",
        lazy.spawn("rofi -show drun -config ~/.config/rofi/dmenu.rasi -display-drun Run:"),
        desc= "run dmenu style launcher"
        ),
    Key([mod, "shift"], "o",
        lazy.spawn("~/.config/rofi/launchers/ribbon/launcher.sh &"),
        desc= "Spawn default browser"
        ),
    Key([mod], "f",
        lazy.window.toggle_fullscreen(),
        desc= "Toggle fullscreen"
        ),
    Key([mod, "shift"], "f",
        lazy.spawn("firefox"),
        desc= "Spawn default browser"
        ),
    Key([mod, "shift"], "j",
        lazy.spawn("/home/dom/.joplin/Joplin.AppImage"),
        desc= "Spawn default browser"
        ),
    Key([mod], "b",
        lazy.spawn("brave"),
        ),
    Key([mod, "shift"], "b",
        lazy.spawn("google-chrome-stable"),
        ),
    # Key([mod], "f",
    #     lazy.spawn("brave"),
    #     desc= "Spawn firefox"
    #     ),
    Key([mod], "e",
        lazy.spawn("nemo"),
        desc= "spawn file manager"
        ),
    Key([mod], "Tab",
        lazy.spawn("rofi -theme ~/.config/rofi/configTall.rasi -show window"),
        desc= "spawn file manager"
        ),
    # Monitor controls
     Key([mod], "a",
         lazy.to_screen(0),
         desc='Keyboard focus to monitor 1'
         ),
     Key([mod], "s",
         lazy.to_screen(1),
         desc='Keyboard focus to monitor 2'
         ),

    # layout controls

    # windows controls

    # stack controls

    Key([mod], "q", lazy.window.kill()),
    # Key([mod], "v", lazy.spawn('pavucontrol')),
    Key([mod], "x", lazy.spawn('arcolinux-logout')),
    Key([mod], "Escape", lazy.spawn('xkill')),
    Key([mod], "F5", lazy.spawn('meld')),
    Key([mod], "F6", lazy.spawn('vlc --video-on-top')),
    Key([mod], "F7", lazy.spawn('virtualbox')),
    Key([mod], "F10", lazy.spawn("spotify")),

    Key([mod, "shift"], "q", lazy.window.kill()),
    Key([mod, "shift"], "r", lazy.restart()),
    Key([mod, "control"], "r", lazy.restart()),


    # Key([], "Print", lazy.spawn("scrot 'ArcoLinux-%Y-%m-%d-%s_screenshot_$wx$h.jpg' -e 'mv $f $$(xdg-user-dir PICTURES)'")),
    Key([], "Print", lazy.spawn("flameshot gui -p /home/dom/Pictures")),

# INCREASE/DECREASE BRIGHTNESS
    Key([], "XF86MonBrightnessUp", lazy.spawn("xbacklight -inc 5")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("xbacklight -dec 5")),

# INCREASE/DECREASE/MUTE VOLUME
    Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -q set Master 5%-")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -q set Master 5%+")),

    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next")),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous")),
    Key([], "XF86AudioStop", lazy.spawn("playerctl stop")),

#    Key([], "XF86AudioPlay", lazy.spawn("mpc toggle")),
#    Key([], "XF86AudioNext", lazy.spawn("mpc next")),
#    Key([], "XF86AudioPrev", lazy.spawn("mpc prev")),
#    Key([], "XF86AudioStop", lazy.spawn("mpc stop")),

# QTILE LAYOUT KEYS
    Key([mod], "n", lazy.layout.normalize()),
    Key([mod], "space", lazy.next_layout()),

# CHANGE FOCUS
    Key([mod], "Up", lazy.layout.up()),
    Key([mod], "Down", lazy.layout.down()),
    Key([mod], "Left", lazy.layout.left()),
    Key([mod], "Right", lazy.layout.right()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),


# RESIZE UP, DOWN, LEFT, RIGHT
    Key([mod, "control"], "l",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        ),
    Key([mod, "control"], "Right",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        ),
    Key([mod, "control"], "h",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        ),
    Key([mod, "control"], "Left",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        ),
    Key([mod, "control"], "k",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        ),
    Key([mod, "control"], "Up",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        ),
    Key([mod, "control"], "j",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        ),
    Key([mod, "control"], "Down",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        ),


# FLIP LAYOUT FOR MONADTALL/MONADWIDE
    # Key([mod, "shift"], "f", lazy.layout.flip()),

# FLIP LAYOUT FOR BSP
    # Key([mod, "mod1"], "k", lazy.layout.flip_up()),
    # Key([mod, "mod1"], "j", lazy.layout.flip_down()),
    # Key([mod, "mod1"], "l", lazy.layout.flip_right()),
    # Key([mod, "mod1"], "h", lazy.layout.flip_left()),

# MOVE WINDOWS UP OR DOWN BSP LAYOUT
    # Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
    # Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    # Key([mod, "shift"], "h", lazy.layout.shuffle_left()),
    # Key([mod, "shift"], "l", lazy.layout.shuffle_right()),

# MOVE WINDOWS UP OR DOWN MONADTALL/MONADWIDE LAYOUT
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "Left", lazy.layout.swap_left()),
    Key([mod, "shift"], "Right", lazy.layout.swap_right()),

# TOGGLE FLOATING LAYOUT
    Key([mod, "shift"], "space", lazy.window.toggle_floating()),]

groups = [
    Group(
        "1",
        layout="monadtall",
        label=""
    ),
    Group(
        "2",
        matches=[Match(wm_class=["firefox"])],
        layout="monadtall",
        label=""
    ),
    Group(
        "3",
        layout="monadtall",
        label=""
    ),
    Group(
        "4",
        # label=""
        layout="monadtall",
        matches=[Match(wm_class=["Virtualbox"])],
        label=""
    ),
    Group(
        "5",
        matches=[Match(wm_class=["Thunderbird"])],
        layout="monadtall",
        label=""
    ),
    Group(
      "6",
        layout="monadtall",
        label=""
    ),
    Group(
        "7",
        layout="monadtall",
        label=""
    ),
    ]


for i in groups:
    keys.extend([
#CHANGE WORKSPACES
        Key([mod], i.name, lazy.group[i.name].toscreen()),
        # Key([mod], "Tab", lazy.screen.next_group()),
        Key(["mod1"], "Tab", lazy.screen.next_group()),
        Key(["mod1", "shift"], "Tab", lazy.screen.prev_group()),

# MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND STAY ON WORKSPACE
        #Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
# MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND FOLLOW MOVED WINDOW TO WORKSPACE
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name) , lazy.group[i.name].toscreen()),
    ])


def open_pavu():
    qtile.cmd_spawn("pavucontrol")

layout_theme = {
    "border_width": 2,
    "margin": 3,
    "border_focus": "#5e81ac",
    "border_normal": "3b4252",
    "font": "FiraCode Nerd Font",
    }

layouts = [
        #layout.MonadWide(**layout_theme),
        layout.Bsp(**layout_theme),
        #layout.Stack(stacks=2, **layout_theme),
        #layout.Columns(**layout_theme),
        #layout.RatioTile(**layout_theme),
        #layout.VerticalTile(**layout_theme),
        #layout.Matrix(**layout_theme),
        #layout.Zoomy(**layout_theme),
        # layout.MonadTall(margin=8, border_width=2, border_focus="#5e81ac", border_normal="#4c566a"),
        layout.MonadTall(**layout_theme),
        layout.Max(**layout_theme),
        # layout.Tile(shift_windows=True, **layout_theme),
        # layout.Stack(num_stacks=2),
        # layout.TreeTab(
        #      font = "Ubuntu",
        #      fontsize = 10,
        #      sections = ["FIRST", "SECOND"],
        #      section_fontsize = 11,
        #      bg_color = "141414",
        #      active_bg = "90C435",
        #      active_fg = "000000",
        #      inactive_bg = "384323",
        #      inactive_fg = "a0a0a0",
        #      padding_y = 5,
        #      section_top = 10,
        #      panel_width = 320
        #      ),
        layout.Floating(**layout_theme)
]


# colors = dict(
#         bg_dark= "#2E3440",
#         bg_light= "#88C0D0",
#         bg_focused= "#3B4252",
#         fg_unused= "#4C566A",
#         fg_used= "#D8Dee9",
#         fg_highlight= "#D08770"
#         ) 

colors = [
    ["#2e3440", "#2e3440"],  # background
    ["#d8dee9", "#d8dee9"],  # foreground
    ["#3b4252", "#3b4252"],  # background lighter
    ["#bf616a", "#bf616a"],  # red
    ["#a3be8c", "#a3be8c"],  # green
    ["#ebcb8b", "#ebcb8b"],  # yellow
    ["#81a1c1", "#81a1c1"],  # blue
    ["#b48ead", "#b48ead"],  # magenta
    ["#88c0d0", "#88c0d0"],  # cyan
    ["#e5e9f0", "#e5e9f0"],  # white
    ["#4c566a", "#4c566a"],  # grey
    ["#d08770", "#d08770"],  # orange
    ["#8fbcbb", "#8fbcbb"],  # super cyan
    ["#5e81ac", "#5e81ac"],  # super blue
    ["#242831", "#242831"],  # super dark background
]


# WIDGETS FOR THE BAR
widget_defaults = dict(
    font="FiraCode Nerd Font", fontsize=18, padding=3, background=colors[0]
)
extension_defaults = widget_defaults.copy()

group_box_settings = {
    "padding": 5,
    "borderwidth": 4,
    "active": colors[1],
    "inactive": colors[10],
    "disable_drag": True,
    "rounded": True,
    "highlight_color": colors[0],
    "block_highlight_text_color": colors[8],
    "highlight_method": "line",
    "this_current_screen_border": colors[8],
    "this_screen_border": colors[1],
    "other_current_screen_border": colors[0],
    "other_screen_border": colors[0],
    "foreground": colors[1],
    "background": colors[0],
}


def init_widgets_list():
    # prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())
    widgets_list = [
        widget.Sep(
            linewidth=20,
            foreground=colors[0],
            background=colors[0],
            padding=10,
            size_percent=40,
        ),
        widget.CurrentLayoutIcon(
            custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons")],
            foreground=colors[2],
            background=colors[0],
            padding=-2,
            scale=0.45,
        ),
        widget.Sep(
            linewidth=20,
            foreground=colors[0],
            background=colors[0],
            padding=10,
            size_percent=40,
        ),
        widget.GroupBox(
            **group_box_settings
        ),
        widget.Spacer(),
        widget.TextBox(
            text=" ",
            foreground=colors[12],
            background=colors[0],
            # fontsize=38,
            font="Font Awesome 5 Free Solid",
        ),
        # TODO: can i actually make that to an impressive tasklist?
        CustomWindowName(
            background=colors[0],
            foreground=colors[12],
            width=bar.CALCULATED,
            empty_group_string="Desktop",
            max_chars=165,
            # mouse_callbacks={"Button2": kill_window},
        ),
        widget.Spacer(),
        widget.CheckUpdates(
            background=colors[0],
            foreground=colors[3],
            colour_have_updates=colors[3],
            custom_command="./.config/qtile/updates-arch-combined",
            display_format=" {updates}",
            # execute=update,
            padding=20,
        ),
        # widget.GenPollText(
        #    func=updates,
        #    update_interval=300,
        #    foreground=colors[3],
        #    mouse_callbacks={"Button1": update},
        # ),
        widget.Sep(
            linewidth=20,
            foreground=colors[0],
            padding=10,
            size_percent=50,
        ),
        widget.TextBox(
            text=" ",
            foreground=colors[8],
            background=colors[0],
            font="Font Awesome 5 Free Solid",
            # fontsize=38,
        ),
        widget.PulseVolume(
            foreground=colors[8],
            background=colors[0],
            limit_max_volume="True",
            mouse_callbacks={"Button3": open_pavu},
        ),
        widget.Sep(
            linewidth=20,
            foreground=colors[0],
            padding=10,
            size_percent=50,
        ),
        # TODO: enable Bluetooth and WLAN for notebook
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
        # widget.TextBox(
        #     text=" ",
        #     font="Font Awesome 5 Free Solid",
        #     foreground=colors[7],  # fontsize=38
        #     background=colors[14],
        # ),
        # widget.Wlan(
        #     interface="wlan0",
        #     format="{essid}",
        #     foreground=colors[7],
        #     background=colors[14],
        #     padding=5,
        #     # mouse_callbacks={"Button1": open_connman},
        # ),
        # widget.TaskList(
        #    fontsize=14,
        #    background=colors[0],
        #    border=colors[2],
        #    borderwidth=0,
        #    highlight_method="block",
        #    icon_size=0,
        #    margin_y=3,
        #    margin_x=3,
        #    padding_x=3,
        #    padding_y=3,
        #    spacing=0,
        #    # max_title_width=24,
        #    # markup_floating="",
        #    # markup_focused="<span underline=”low”>{}</span>",
        #    # markup_maximized="",
        #    # markup_minimized="",
        #    # markup_normal="",
        # ),
        # widget.Spacer(),
        # widget.Systray(
        #     padding=5,
        #     background=colors["bg_light"]
        # ),
        # widget.TextBox(
        #     text="  ",
        #     background=colors["bg_light"],
        #     foreground=colors["bg_dark"]
        # ),
        # widget.TextBox(
        #     # **separator_defaults,
        #     text=left_sep,
        #     font="FiraCode Nerd Font Mono",
        #     fontsize=57,
        #     padding=0,
        #     background=colors["bg_light"],
        #     foreground=colors["bg_dark"]
        # ),
        # widget.Volume(
        #     step=5,
        #     padding=0,
        #     margin=0,
        #     theme_path=TELA_ICONS+"24/panel/",
        #     volume_app="pavucontrol",
        #     background=colors["volume_bg"],
        # ),
       # widget.TextBox(
       #          font="FontAwesome",
       #          text="  ",
       #          foreground=colors["fg_used"],
       #          background=colors["bg_dark"],
       #          padding = 0,
       #          fontsize=16
       #          ),
       # widget.Memory(
       #          font="Noto Sans",
       #          format = '{MemUsed}M/{MemTotal}M',
       #          update_interval = 1,
       #          fontsize = 12,
       #          foreground = colors["fg_used"],
       #          background = colors["bg_dark"],
       #         ),
        # widget.TextBox(
            # # **separator_defaults,
            # text=sep,
            # foreground=colors["fg_unused"],
            # background=colors["bg_dark"],
            # fontsize=37
        # ),
        # widget.TextBox(
        #     # **separator_defaults,
        #     text=sep,
        #     foreground=colors["fg_unused"],
        #     background=colors["bg_dark"],
        #     fontsize=37
        # ),
        # widget.Net(
        #      interface = "enp2s0",
        #      format = '{down} ↓↑ {up}',
        #      foreground = colors["fg_used"],
        #      background = colors["bg_dark"],
        #      padding = 5
        # ),
      # widget.TextBox(
      #          text = " ⟳",
      #          padding = 2,
      #          foreground = colors["fg_used"],
      #          background = colors["bg_dark"],
      #          fontsize = 14
      #          ),
      #   widget.Pacman(
      #          update_interval = 1800,
      #          foreground = colors["fg_used"],
      #          mouse_callbacks = {'Button1': lambda qtile: qtile.cmd_spawn(myTerminal + ' -e sudo pacman -Syu')},
      #          background = colors["bg_dark"]
      #   ),
      # widget.TextBox(
      #          text = "Updates",
      #          padding = 5,
      #          mouse_callbacks = {'Button1': lambda qtile: qtile.cmd_spawn(myTerminal + ' -e sudo pacman -Syu')},
      #          foreground = colors["fg_used"],
      #          background = colors["bg_dark"]
      #          ),
        widget.TextBox(
            text=" ",
            font="Font Awesome 5 Free Solid",
            foreground=colors[5],  # fontsize=38
            background=colors[0],
        ),
        widget.Clock(
            format="%a, %b %d",
            background=colors[0],
            foreground=colors[5],
        ),
        widget.Sep(
            linewidth=20,
            foreground=colors[0],
            padding=10,
            size_percent=50,
        ),
        widget.TextBox(
            text=" ",
            font="Font Awesome 5 Free Solid",
            foreground=colors[4],  # fontsize=38
            background=colors[0],
        ),
        widget.Clock(
            format="%H:%M",
            foreground=colors[4],
            background=colors[0],
            # mouse_callbacks={"Button1": todays_date},
        ),
        widget.Sep(
            linewidth=20,
            foreground=colors[0],
            padding=10,
            size_percent=50,
        ),
               # widget.Systray(
               #          background=colors[1],
               #          icon_size=20,
               #          padding = 4
               #          ),
              ]
    return widgets_list

widgets_list = init_widgets_list()

def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    return widgets_screen1

def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    return widgets_screen2

widgets_screen1 = init_widgets_screen1()
widgets_screen2 = init_widgets_screen2()


def init_screens():
    return [Screen(top=bar.Bar(init_widgets_screen1(), 32, margin=[0, -4, 21, -4]), bottom=bar.Gap(18), left=bar.Gap(18), right=bar.Gap(18)),
            Screen(top=bar.Bar(init_widgets_screen1(), 32, margin=[0, -4, 21, -4]), bottom=bar.Gap(18), left=bar.Gap(18), right=bar.Gap(18))]
screens = init_screens()


# MOUSE CONFIGURATION
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size())
]

dgroups_key_binder = None
dgroups_app_rules = []

# ASSIGN APPLICATIONS TO A SPECIFIC GROUPNAME
# BEGIN

# @hook.subscribe.client_new
# def assign_app_group(client):
#     d = {}
#     #########################################################
#     ################ assgin apps to groups ##################
#     #########################################################
#     d["1"] = ["Navigator", "Firefox", "Vivaldi-stable", "Vivaldi-snapshot", "Chromium", "Google-chrome", "Brave", "Brave-browser",
#               "navigator", "firefox", "vivaldi-stable", "vivaldi-snapshot", "chromium", "google-chrome", "brave", "brave-browser", ]
#     d["2"] = [ "Atom", "Subl3", "Geany", "Brackets", "Code-oss", "Code", "TelegramDesktop", "Discord",
#                "atom", "subl3", "geany", "brackets", "code-oss", "code", "telegramDesktop", "discord", ]
#     d["3"] = ["Inkscape", "Nomacs", "Ristretto", "Nitrogen", "Feh",
#               "inkscape", "nomacs", "ristretto", "nitrogen", "feh", ]
#     d["4"] = ["Gimp", "gimp" ]
#     d["5"] = ["Meld", "meld", "org.gnome.meld" "org.gnome.Meld" ]
#     d["6"] = ["Vlc","vlc", "Mpv", "mpv" ]
#     d["7"] = ["VirtualBox Manager", "VirtualBox Machine", "Vmplayer",
#               "virtualbox manager", "virtualbox machine", "vmplayer", ]
#     d["8"] = ["Thunar", "Nemo", "Caja", "Nautilus", "org.gnome.Nautilus", "Pcmanfm", "Pcmanfm-qt",
#               "thunar", "nemo", "caja", "nautilus", "org.gnome.nautilus", "pcmanfm", "pcmanfm-qt", ]
#     d["9"] = ["Evolution", "Geary", "Mail", "Thunderbird",
#               "evolution", "geary", "mail", "thunderbird" ]
#     d["0"] = ["Spotify", "Pragha", "Clementine", "Deadbeef", "Audacious",
#               "spotify", "pragha", "clementine", "deadbeef", "audacious" ]
#     ##########################################################
#     wm_class = client.window.get_wm_class()[0]
#
#     for i in range(len(d)):
#         if wm_class in list(d.values())[i]:
#             group = list(d.keys())[i]
#             client.togroup(group)
#             client.group.cmd_toscreen()

# END
# ASSIGN APPLICATIONS TO A SPECIFIC GROUPNAME



main = None

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/scripts/autostart.sh'])

@hook.subscribe.startup
def start_always():
    # Set the cursor to something sane in X
    subprocess.Popen(['xsetroot', '-cursor_name', 'left_ptr'])

@hook.subscribe.client_new
def set_floating(window):
    if (window.window.get_wm_transient_for()
            or window.window.get_wm_type() in floating_types):
        window.floating = True

floating_types = ["notification", "toolbar", "splash", "dialog"]


# follow_mouse_focus = True
dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"

floating_layout = layout.Floating(float_rules=[
    {'wmclass': 'Arcolinux-welcome-app.py'},
    {'wmclass': 'Arcolinux-tweak-tool.py'},
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},
    {'wmclass': 'makebranch'},
    {'wmclass': 'maketag'},
    {'wmclass': 'Arandr'},
    {'wmclass': 'feh'},
    {'wmclass': 'Galculator'},
    {'wmclass': 'arcolinux-logout'},
    {'wmclass': 'xfce4-terminal'},
    {'wname': 'branchdialog'},
    {'wname': 'Open File'},
    {'wname': 'pinentry'},
    {'wmclass': 'ssh-askpass'},

],  fullscreen_border_width = 0, border_width = 0)


wmname = "LG3D"

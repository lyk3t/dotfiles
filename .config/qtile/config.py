import os
import re
import socket
import subprocess
from libqtile.config import Drag, Key, Screen, Match, Group, Drag, Click, Rule
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
from libqtile.widget import Spacer

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
    # Key([mod], "KP Enter",
    #     lazy.spawn(myTerminal),
    #     desc= "Run Terminal"
    #     ),
    Key([mod, "shift"], "Return",
        lazy.spawn("rofi -show drun -config ~/.config/rofi/themes/menu.rasi -display-drun \"Run: \" -drun-display-format \"{name}\""),
        desc= "Run Launcher"
        ),
    Key([mod], "f",
        lazy.window.toggle_fullscreen(),
        desc= "Toggle fullscreen"
        ),
    Key([mod], "b",
        lazy.spawn("brave"),
        desc= "Spawn default browser"
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
        lazy.spawn("rofi -show window"),
        desc= "spawn file manager"
        ),
    # rofi window manager
    # rofi center

    # application spawns

    # Monitor controls

    # layout controls

    # windows controls

    # stack controls
# SUPER + FUNCTION KEYS

    # Key([mod], "e", lazy.spawn('atom')),
    # Key([mod], "c", lazy.spawn('conky-toggle')),
    # Key([mod], "m", lazy.spawn('pragha')),
    Key([mod], "q", lazy.window.kill()),
    # Key([mod], "r", lazy.spawn('rofi-theme-selector')),
    # Key([mod], "t", lazy.spawn('urxvt')),
    # Key([mod], "v", lazy.spawn('pavucontrol')),
    # Key([mod], "w", lazy.spawn('vivaldi-stable')),
    Key([mod], "x", lazy.spawn('arcolinux-logout')),
    Key([mod], "Escape", lazy.spawn('xkill')),
    # Key([mod], "F1", lazy.spawn('vivaldi-stable')),
    # Key([mod], "F2", lazy.spawn('atom')),
    # Key([mod], "F3", lazy.spawn('inkscape')),
    # Key([mod], "F4", lazy.spawn('gimp')),
    Key([mod], "F5", lazy.spawn('meld')),
    Key([mod], "F6", lazy.spawn('vlc --video-on-top')),
    Key([mod], "F7", lazy.spawn('virtualbox')),
    # Key([mod], "F8", lazy.spawn('thunar')),
    # Key([mod], "F9", lazy.spawn('evolution')),
    Key([mod], "F10", lazy.spawn("spotify")),
    # Key([mod], "F11", lazy.spawn('rofi -show run -fullscreen')),
    # Key([mod], "F12", lazy.spawn('rofi -show run')),

# SUPER + SHIFT KEYS

    # Key([mod, "shift"], "Return", lazy.spawn('thunar')),
    # Key([mod, "shift"], "d", lazy.spawn("dmenu_run -i -nb '#191919' -nf '#fea63c' -sb '#fea63c' -sf '#191919' -fn 'NotoMonoRegular:bold:pixelsize=14'")),
    Key([mod, "shift"], "q", lazy.window.kill()),
    Key([mod, "shift"], "r", lazy.restart()),
    Key([mod, "control"], "r", lazy.restart()),
    # Key([mod, "shift"], "x", lazy.shutdown()),

# CONTROL + ALT KEYS

    Key(["mod1", "control"], "Next", lazy.spawn('conky-rotate -n')),
    Key(["mod1", "control"], "Prior", lazy.spawn('conky-rotate -p')),
    # Key(["mod1", "control"], "a", lazy.spawn('xfce4-appfinder')),
    # Key(["mod1", "control"], "b", lazy.spawn('thunar')),
    # Key(["mod1", "control"], "c", lazy.spawn('catfish')),
    Key(["mod1", "control"], "e", lazy.spawn('arcolinux-tweak-tool')),
    Key(["mod1", "control"], "f", lazy.spawn('firefox')),
    Key(["mod1", "control"], "g", lazy.spawn('chromium -no-default-browser-check')),
    Key(["mod1", "control"], "i", lazy.spawn('nitrogen')),
    Key(["mod1", "control"], "k", lazy.spawn('arcolinux-logout')),
    Key(["mod1", "control"], "l", lazy.spawn('arcolinux-logout')),
    Key(["mod1", "control"], "m", lazy.spawn('xfce4-settings-manager')),
    Key(["mod1", "control"], "o", lazy.spawn(home + '/.config/qtile/scripts/picom-toggle.sh')),
    # Key(["mod1", "control"], "p", lazy.spawn('pamac-manager')),
    # Key(["mod1", "control"], "r", lazy.spawn('rofi-theme-selector')),
    # Key(["mod1", "control"], "s", lazy.spawn('spotify')),
    # Key(["mod1", "control"], "t", lazy.spawn('termite')),
    # Key(["mod1", "control"], "u", lazy.spawn('pavucontrol')),
    # Key(["mod1", "control"], "v", lazy.spawn('vivaldi-stable')),
    Key(["mod1", "control"], "w", lazy.spawn('arcolinux-welcome-app')),
    # Key(["mod1", "control"], "Return", lazy.spawn('termite')),

# ALT + ... KEYS

    # Key(["mod1"], "f", lazy.spawn('variety -f')),
    Key(["mod1"], "h", lazy.spawn('urxvt -e htop')),
    # Key(["mod1"], "n", lazy.spawn('variety -n')),
    # Key(["mod1"], "p", lazy.spawn('variety -p')),
    # Key(["mod1"], "t", lazy.spawn('variety -t')),
    # Key(["mod1"], "Up", lazy.spawn('variety --pause')),
    # Key(["mod1"], "Down", lazy.spawn('variety --resume')),
    # Key(["mod1"], "Left", lazy.spawn('variety -p')),
    # Key(["mod1"], "Right", lazy.spawn('variety -n')),
    # Key(["mod1"], "F2", lazy.spawn('gmrun')),
    # Key(["mod1"], "F3", lazy.spawn('xfce4-appfinder')),

# VARIETY KEYS WITH PYWAL

    # Key(["mod1", "shift"], "f", lazy.spawn(home + '/.config/qtile/scripts/set-pywal.sh -f')),
    # Key(["mod1", "shift"], "p", lazy.spawn(home + '/.config/qtile/scripts/set-pywal.sh -p')),
    # Key(["mod1", "shift"], "n", lazy.spawn(home + '/.config/qtile/scripts/set-pywal.sh -n')),
    # Key(["mod1", "shift"], "u", lazy.spawn(home + '/.config/qtile/scripts/set-pywal.sh -u')),

# CONTROL + SHIFT KEYS

    # Key([mod2, "shift"], "Escape", lazy.spawn('xfce4-taskmanager')),

# SCREENSHOTS

    # Key([], "Print", lazy.spawn("scrot 'ArcoLinux-%Y-%m-%d-%s_screenshot_$wx$h.jpg' -e 'mv $f $$(xdg-user-dir PICTURES)'")),
    Key([], "Print", lazy.spawn("flameshot gui -p /home/dom/Pictures")),
    # Key([mod2], "Print", lazy.spawn('xfce4-screenshooter')),
    # Key([mod2, "shift"], "Print", lazy.spawn('gnome-screenshot -i')),

# MULTIMEDIA KEYS

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
    Key([mod, "shift"], "f", lazy.layout.flip()),

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
        label=""
    ),
    Group(
        "2",
        matches=[Match(wm_class=["firefox"])],
        layout="monadtall",
        label=""
    ),
    Group(
        "3",
        layout="monadtall",
        label=""
    ),
    Group(
        "4",
        # label=""
        layout="max",
        matches=[Match(wm_class=["Virtualbox"])],
        label=""
    ),
    Group(
        "5",
        matches=[Match(wm_class=["Thunderbird"])],
        layout="monadtall",
        label=""
    ),
    Group(
      "6",
        layout="monadtall",
        label=""
    ),
    Group(
        "7",
        layout="monadtall",
        label=""
    ),
    ]

# group_labels = ["", "", "", "", "", "", "", "", "", "",]

# group_layouts = ["monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall",]
#group_layouts = ["monadtall", "matrix", "monadtall", "bsp", "monadtall", "matrix", "monadtall", "bsp", "monadtall", "monadtall",]

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


def init_layout_theme():
    return {"margin":5,
            "border_width":2,
            "border_focus": "#5e81ac",
            "border_normal": "#4c566a"
            }

layout_theme = init_layout_theme()

layouts = [
        #layout.MonadWide(**layout_theme),
        #layout.Bsp(**layout_theme),
        #layout.Stack(stacks=2, **layout_theme),
        #layout.Columns(**layout_theme),
        #layout.RatioTile(**layout_theme),
        #layout.VerticalTile(**layout_theme),
        #layout.Matrix(**layout_theme),
        #layout.Zoomy(**layout_theme),
        # layout.MonadTall(margin=8, border_width=2, border_focus="#5e81ac", border_normal="#4c566a"),
        layout.MonadTall(**layout_theme),
        layout.Max(**layout_theme),
        layout.Tile(shift_windows=True, **layout_theme),
        layout.Stack(num_stacks=2),
        layout.TreeTab(
             font = "Ubuntu",
             fontsize = 10,
             sections = ["FIRST", "SECOND"],
             section_fontsize = 11,
             bg_color = "141414",
             active_bg = "90C435",
             active_fg = "000000",
             inactive_bg = "384323",
             inactive_fg = "a0a0a0",
             padding_y = 5,
             section_top = 10,
             panel_width = 320
             ),
        layout.Floating(**layout_theme)
]


colors = dict(
        bg_dark= "#2E3440",
        bg_light= "#88C0D0",
        bg_focused= "#3B4252",
        fg_unused= "#4C566A",
        fg_used= "#D8Dee9",
        fg_highlight= "#D08770"
        ) 


# WIDGETS FOR THE BAR

widget_defaults = dict(
    font="Hack Nerd Font",
    fontsize = 14,
    padding = 2,
    background=colors["bg_dark"]
)
extension_defaults = widget_defaults.copy()

# left_sep = ""
sep = ""
# right_sep = ""

separator_defaults = dict(
    font="FiraCode Nerd Font Mono",
    fontsize=33,
    padding=0
)

def init_widgets_list():
    # prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())
    widgets_list = [
        widget.GroupBox(
            background=colors["bg_dark"],
            active=colors["fg_used"],
            block_highlight_text_color=colors["bg_light"],
            highlight_color=colors["bg_dark"],
            highlight_method="line",
            borderwidth=0,
            rounded=False,
            inactive=colors["fg_unused"],
            margin_y=3,
            margin_x=2,
            padding_x=8,
            fmt="<b>{}</b>",
            # visible_groups=group_names, # Fix bug of extra groups appearing from default config
        ),
        # widget.TextBox(
        #     # **separator_defaults,
        #     text=right_sep,
        #     font="FiraCode Nerd Font Mono",
        #     fontsize=57,
        #     padding=0,
        #     background=colors["bg_light"],
        #     foreground=colors["bg_dark"]
        # ),
        widget.TaskList(
           fontsize=16,
           background=colors["bg_dark"],
           border=colors["bg_focused"],
           borderwidth=2,
           highlight_method="block",
           # icon_size=20,
           margin_y=3,
           margin_x=3,
           padding_x=3,
           padding_y=3,
           spacing=0,
           # max_title_width=24,
           # markup_floating="",
           # markup_focused="<span underline=”low”>{}</span>",
           # markup_maximized="",
           # markup_minimized="",
           # markup_normal="",
        ),
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
       widget.TextBox(
                font="FontAwesome",
                text="  ",
                foreground=colors["fg_used"],
                background=colors["bg_dark"],
                padding = 0,
                fontsize=16
                ),
       widget.Memory(
                font="Noto Sans",
                format = '{MemUsed}M/{MemTotal}M',
                update_interval = 1,
                fontsize = 12,
                foreground = colors["fg_used"],
                background = colors["bg_dark"],
               ),
        widget.TextBox(
            # **separator_defaults,
            text=sep,
            foreground=colors["fg_unused"],
            background=colors["bg_dark"],
            fontsize=37
        ),
        widget.Net(
             interface = "enp2s0",
             format = '{down} ↓↑ {up}',
             foreground = colors["fg_used"],
             background = colors["bg_dark"],
             padding = 5
        ),
        widget.TextBox(
            # **separator_defaults,
            text=sep,
            foreground=colors["fg_unused"],
            background=colors["bg_dark"],
            fontsize=37
        ),
      widget.TextBox(
               text = " ⟳",
               padding = 2,
               foreground = colors["fg_used"],
               background = colors["bg_dark"],
               fontsize = 14
               ),
        widget.Pacman(
               update_interval = 1800,
               foreground = colors["fg_used"],
               mouse_callbacks = {'Button1': lambda qtile: qtile.cmd_spawn(myTerminal + ' -e sudo pacman -Syu')},
               background = colors["bg_dark"]
        ),
      widget.TextBox(
               text = "Updates",
               padding = 5,
               mouse_callbacks = {'Button1': lambda qtile: qtile.cmd_spawn(myTerminal + ' -e sudo pacman -Syu')},
               foreground = colors["fg_used"],
               background = colors["bg_dark"]
               ),
        widget.TextBox(
            # **separator_defaults,
            text=sep,
            foreground=colors["fg_unused"],
            background=colors["bg_dark"],
            fontsize=37
        ),
        widget.TextBox(
            # **separator_defaults,
            text="",
            font="FiraCode Nerd Font Mono",
            fontsize=20,
            padding=0,
            background=colors["bg_dark"],
        ),
        widget.Volume(
            step=5,
            padding=0,
            margin=0,
            volume_app="pavucontrol",
            fmt=" {0} ",
            background=colors["bg_dark"],
        ),
        widget.TextBox(
            # **separator_defaults,
            text=sep,
            foreground=colors["fg_unused"],
            background=colors["bg_dark"],
            fontsize=37
        ),
        widget.Clock(
            background=colors["bg_dark"],
            foreground=colors["fg_used"],
            format='%d %B | %H:%M',
            fmt="<span font_family='Fira Code Nerd Font' size='larger'> </span> {}",
            padding=4,
            mouse_callbacks={'Button1': lambda qtile: qtile.cmd_spawn(calendar)},
        ),
        widget.TextBox(
            # **separator_defaults,
            text=sep,
            foreground=colors["fg_unused"],
            background=colors["bg_dark"],
            fontsize=37
        ),
        widget.CurrentLayoutIcon(
              custom_icon_paths = [os.path.expanduser("~/.config/qtile/icons")],
              foreground = colors["fg_used"],
              background = colors["bg_dark"],
              padding = 0,
              scale = 0.7
        ),
               # widget.GroupBox(font="FontAwesome",
               #          fontsize = 24,
               #          margin_y = 0,
               #          margin_x = 0,
               #          padding_y = 6,
               #          padding_x = 5,
               #          borderwidth = 0,
               #          disable_drag = True,
               #          active = colors[9],
               #          inactive = colors[5],
               #          rounded = False,
               #          this_current_screen_border = colors[8],
               #          foreground = colors[2],
               #          background = colors[1]
               #          ),
               # widget.Prompt(
               #          prompt='Run:',
               #          ),
               # widget.TaskList(
               #          foreground = "2e3440",
               #          border = "5e81ac",
               #          fontsize = 11,
               #          unfocused_border = "b48ead",
               #          highlight_method = "block",
               #          max_title_width=100,
               #          title_width_method="uniform",
               #          icon_size = 13,
               #          rounded=False,
               #      ),        
               # widget.Sep(
               #          linewidth = 1,
               #          padding = 10,
               #          foreground = colors[2],
               #          background = colors[1]
               #          ),
               # widget.Sep(
               #          linewidth = 1,
               #          padding = 10,
               #          foreground = colors[2],
               #          background = colors[1]
               #          ),
               # # widget.WindowName(font="Noto Sans",
               # #          fontsize = 12,
               # #          foreground = colors[5],
               # #          background = colors[1],
               # #          ),
               # widget.Net(
               #          font="Noto Sans",
               #          fontsize=12,
               #          interface="enp0s31f6",
               #          foreground=colors[2],
               #          background=colors[1],
               #          padding = 0,
               #          ),
               # widget.Sep(
               #          linewidth = 1,
               #          padding = 10,
               #          foreground = colors[2],
               #          background = colors[1]
               #          ),
               # widget.NetGraph(
               #          font="Noto Sans",
               #          fontsize=12,
               #          bandwidth="down",
               #          interface="auto",
               #          fill_color = colors[8],
               #          foreground=colors[2],
               #          background=colors[1],
               #          graph_color = colors[8],
               #          border_color = colors[2],
               #          padding = 0,
               #          border_width = 1,
               #          line_width = 1,
               #          ),
              # widget.TextBox(
               #         text = " ⟳",
               #         padding = 2,
               #         foreground = colors[2],
               #         background = colors[4],
               #         fontsize = 14
               #         ),
              # widget.Pacman(
               #         update_interval = 1800,
               #         foreground = colors[2],
               #         mouse_callbacks = {'Button1': lambda qtile: qtile.cmd_spawn(myTerm + ' -e sudo pacman -Syu')},
               #         background = colors[4]
               #         ),
              # widget.TextBox(
               #         text = "Updates",
               #         padding = 5,
               #         mouse_callbacks = {'Button1': lambda qtile: qtile.cmd_spawn(myTerm + ' -e sudo pacman -Syu')},
               #         foreground = colors[2],
               #         background = colors[4]
               #         ),
               # widget.Sep(
               #          linewidth = 1,
               #          padding = 10,
               #          foreground = colors[2],
               #          background = colors[1]
               #          ),
               # widget.TextBox(
               #          font="FontAwesome",
               #          text="  ",
               #          foreground=colors[6],
               #          background=colors[1],
               #          padding = 0,
               #          fontsize=16
               #          ),
               # widget.CPUGraph(
               #          border_color = colors[2],
               #          fill_color = colors[8],
               #          graph_color = colors[8],
               #          background=colors[1],
               #          border_width = 1,
               #          line_width = 1,
               #          core = "all",
               #          type = "box"
               #          ),
               # widget.Sep(
               #          linewidth = 1,
               #          padding = 10,
               #          foreground = colors[2],
               #          background = colors[1]
               #          ),
               # widget.TextBox(
               #          font="FontAwesome",
               #          text="  ",
               #          foreground=colors[4],
               #          background=colors[1],
               #          padding = 0,
               #          fontsize=16
               #          ),
               # widget.Memory(
               #          font="Noto Sans",
               #          format = '{MemUsed}M/{MemTotal}M',
               #          update_interval = 1,
               #          fontsize = 12,
               #          foreground = colors[5],
               #          background = colors[1],
               #         ),
               # widget.Sep(
               #          linewidth = 1,
               #          padding = 10,
               #          foreground = colors[2],
               #          background = colors[1]
               #          ),
               # widget.TextBox(
               #          font="FontAwesome",
               #          text="  ",
               #          foreground=colors[3],
               #          background=colors[1],
               #          padding = 0,
               #          fontsize=16
               #          ),
               # widget.Clock(
               #          foreground = colors[5],
               #          background = colors[1],
               #          fontsize = 12,
               #          format="%Y-%m-%d %H:%M"
               #          ),
               # widget.Sep(
               #          linewidth = 1,
               #          padding = 10,
               #          foreground = colors[2],
               #          background = colors[1]
               #          ),
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
    return [Screen(top=bar.Bar(widgets=init_widgets_screen1(), size=26)),
            Screen(top=bar.Bar(widgets=init_widgets_screen2(), size=26))]
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

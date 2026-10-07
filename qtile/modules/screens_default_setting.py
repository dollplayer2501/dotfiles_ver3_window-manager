"""
Built-in Widgets
================

Built-in Widgets — Qtile
https://docs.qtile.org/en/latest/manual/ref/widgets.html
"""

#
#
#

from libqtile import bar, qtile, widget
from libqtile.config import Screen
#
from modules.variables import (
  default_wallpaper,
)
from modules.screens_default_config import (
  sep_args,
  prompt_args,
  chord_args,
  currentLayout_args,
  groupBox_args,
  windowTabs_args,
  CPU_args,
  thermalSensor_args,
  genPollText_GPU_args,
  memory_args,
  checkUpdates_args,
  genPollText_uptime_args,
  volume_widget,
  volume_args,
  clock_args,
  systray_args,
  textBox_power_menu_args,
)
from theme_colors import Theme_Colors


#
#
#

screens = [
  Screen(
    #
    # TODO: 2026-10-05
    #   Are the wallpaper-related settings not specific to qtile-extras?
    #
    wallpaper = default_wallpaper,
    wallpaper_mode = 'fill',

    top = None,

    bottom = bar.Bar(
      [
        widget.Prompt(**prompt_args,),
        widget.Chord(**chord_args,),
        widget.CurrentLayout(**currentLayout_args,),
        widget.Sep(**sep_args, size_percent = 70,),
        widget.GroupBox(**groupBox_args,),
        widget.Sep(**sep_args, size_percent = 100,),
        widget.WindowTabs(**windowTabs_args,),
        widget.Sep(**sep_args, size_percent = 100,),
        widget.CPU(**CPU_args,),
        widget.ThermalSensor(**thermalSensor_args,),
        widget.GenPollText(**genPollText_GPU_args,),
        widget.Memory(**memory_args,),
        widget.Sep(**sep_args, size_percent = 70,),
        widget.CheckUpdates(**checkUpdates_args,),
        widget.GenPollText(**genPollText_uptime_args,),
        widget.Sep(**sep_args, size_percent = 70,),
        volume_widget(**volume_args,),
        widget.Sep(**sep_args, size_percent = 100,),
        widget.Clock(**clock_args,),
        widget.Sep(**sep_args, size_percent = 100,),
        widget.Systray(**systray_args,),
        widget.Sep(**sep_args, size_percent = 100,),
        widget.TextBox(**textBox_power_menu_args,),
        # NOTE: About This widget
        #   > busctl --user status org.freedesktop.Notifications
        #   I use `/usr/lib/xfce4/notifyd/xfce4-notifyd`
        #   > pkill xfce4-notifyd
        #   > pgrep -a xfce4-notifyd
        #   **Reload Qtile**
        #   > notify-send "hoge"
        #   Text is displayed on the Qtile widget. (Hmm... I wonder...)
        #   Tentative conclusion:
        #     I installed Xfce4 first and use Qtile within that environment.
        #     I launch `xfce4-notifyd.service` via `script/autostart.sh`,
        #     but I suspect it isn't actually being controlled from there.
        # widget.Notify(),
      ],
      24,
      border_width = [1, 0, 1, 0],
      border_color = [Theme_Colors['Oreange'], Theme_Colors['Oreange'], Theme_Colors['Oreange'], Theme_Colors['Oreange']],
      margin = [0, 0, 0, 0],
      #
      # TODO: 2026-10-05
      #   This opacity setting isn't taking effect. I haven't investigated yet whether it's related to Picom.
      #
      opacity = 0.70,
    ),
  ),
  # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
  # By default we handle these events delayed to already improve performance, however your system might still be struggling
  # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
  # x11_drag_polling_rate = 60,
]


##


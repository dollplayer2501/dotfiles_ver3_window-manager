"""
Built-in Widgets
================

Built-in Widgets — Qtile
https://docs.qtile.org/en/latest/manual/ref/widgets.html

Widgets — qtile-extras
https://qtile-extras.readthedocs.io/en/stable/manual/ref/widgets.html
"""

#
#
#

from libqtile import bar, qtile
from libqtile.config import Screen
from libqtile.lazy import lazy

from qtile_extras import widget # from libqtile import widget
from qtile_extras.widget.decorations import PowerLineDecoration

from modules.variables import (
  default_wallpaper,
)
from modules.screens_default_config import (
  common_powerline,
  prompt_args,
  chord_args,
  currentLayoutIcon_args,
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
    wallpaper = default_wallpaper,
    wallpaper_mode = 'fill',
    top = None,

    bottom = bar.Bar(
      [
        widget.Prompt(**prompt_args,),
        widget.Chord(**chord_args,),
        widget.CurrentLayoutIcon(**currentLayoutIcon_args,),
        widget.GroupBox(**groupBox_args, **common_powerline,),
        widget.WindowTabs(**windowTabs_args,),
        widget.CPU(**CPU_args,),
        widget.ThermalSensor(**thermalSensor_args,),
        widget.GenPollText(**genPollText_GPU_args,),
        widget.Memory(**memory_args,),
        widget.CheckUpdates(**checkUpdates_args,),
        widget.GenPollText(**genPollText_uptime_args,),
        volume_widget(**volume_args, **common_powerline,),
        widget.Clock(**clock_args, **common_powerline,),
        widget.Systray(**systray_args, **common_powerline,),
        widget.TextBox(**textBox_power_menu_args,),
      ],
      24,
      border_width = [1, 0, 1, 0],
      border_color = [Theme_Colors['Oreange'], Theme_Colors['Oreange'], Theme_Colors['Oreange'], Theme_Colors['Oreange']],
      margin = [0, 0, 0, 0],
      opacity = 0.70,
    ),
  ),
  # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
  # By default we handle these events delayed to already improve performance, however your system might still be struggling
  # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
  # x11_drag_polling_rate = 60,
]


##


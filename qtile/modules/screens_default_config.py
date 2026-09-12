#
#
#

import subprocess

from qtile_extras.widget.decorations import PowerLineDecoration
from qtile_extras import widget # from libqtile import widget
from libqtile.lazy import lazy

from modules.popup import (
  show_power_menu,
)
from modules.functions import (
  get_uptime,
  get_gpu_usage,
)
from modules.variables import (
  my_hostname,
  hostname_chandanna,
  hostname_bacstual,
  font_set,
  current_gengou_reiwa,
  custom_layout_icon_path,
  workspace_main,
)
from theme_colors import Theme_Colors


#
# https://qtile-extras.readthedocs.io/en/stable/manual/ref/decorations.html#powerlinedecoration
#
common_powerline = {
  'decorations': [
    PowerLineDecoration(
      extrawidth = 0,
      ignore_extrawidth = True,
      stroke_colour = Theme_Colors['Oreange'],
      stroke_weight = 1,
      path = 'forward_slash',
    )
  ]
}

#
# https://docs.qtile.org/en/latest/manual/ref/widgets.html#prompt
#
prompt_args = {
  'prompt': 'I Ran (So Far Away): ',

  'fontsize': 20,
  'font': font_set['sub2'],

  'cursor_color': Theme_Colors['DarkBlue_default'],
  'foreground': Theme_Colors['DarkBlue_default'],
  'background': Theme_Colors['Oreange'],
}

#
# https://docs.qtile.org/en/latest/manual/ref/widgets.html#chord
#
chord_args = {
  'fontsize': 20,
  'font': font_set['sub2'],

  'foreground': Theme_Colors['DarkBlue_default'],
  'background': Theme_Colors['Oreange'],

  # TODO: Pend
  # chords_colors = {
  #   'Applications': (
  #     # Theme_Colors['Oreange'],
  #     Theme_Colors['Debug'],
  #     # Theme_Colors['DarkBlue_default'],
  #   ),
  # },
}

#
# https://docs.qtile.org/en/latest/manual/ref/widgets.html#currentlayout
#
currentLayoutIcon_args = {
  'custom_icon_paths': custom_layout_icon_path,

  'scale': 0.8,
  'padding': 4,

  'foreground': Theme_Colors['Debug'],
  'background': Theme_Colors['DarkBlue_default'],
}

#
# https://docs.qtile.org/en/latest/manual/ref/widgets.html#groupbox
#
groupBox_args = {
  'visible_groups': workspace_main,

  'fontsize': 16,
  'font': font_set['main'],

  'margin': 0,
  'margin_x': 0,
  'margin_y': 4,

  'active': Theme_Colors['LightBlue'],
  'block_highlight_text_color': Theme_Colors['Oreange'],
  'borderwidth': 0,

  'inactive': Theme_Colors['Purple'],
  'foreground': Theme_Colors['Debug'],
  'background': Theme_Colors['DarkBlue_default'],
}

#
# https://docs.qtile.org/en/latest/manual/ref/widgets.html#windowtabs
#
windowTabs_args = {
  'fontsize': 14,
  'font': font_set['sub1'],
  'padding': 2,
  'separator': ' | ',

  # NOTE: 2026-03-30
  # If I want to utilize `max_chars`, I need to suppress the functionality of `markup`.
  # 'max_chars': 50,
  'max_chars': 0,
  'markup': True,
  'fmt': '{}',
  'selected': ('<span size="14pt" foreground="' + Theme_Colors['Oreange'] + '">', '</span>'),

  'foreground': Theme_Colors['LightBlue'],
  'background': Theme_Colors['DarkBlue_default'],
}

#
# https://docs.qtile.org/en/latest/manual/ref/widgets.html#cpu
#
CPU_args = {
  # 'format': '<small>CPU</small> {load_percent}% <small>{freq_current}GHz</small>',
  'format': '<small>CPU</small> {load_percent}%',
  'update_interval': 2, # seconds ?

  'padding': 2,
  'fontsize': 18,
  'font': font_set['main'],

  'foreground': Theme_Colors['LightBlue'],
  'background': Theme_Colors['DarkBlue_default'],
}

#
# https://docs.qtile.org/en/latest/manual/ref/widgets.html#thermalsensor
#
thermalSensor_args = {
  # NOTE: This need `lm_sensors` package.
  #       And check `sensors`.

  'tag_sensor': 'Tctl',
  'update_interval': 2, # seconds
  'threshold': 45,

  'padding': 2,
  'fontsize': 14,
  'font': font_set['main'],

  'foreground': Theme_Colors['LightBlue'],
  'foreground_alert': Theme_Colors['Oreange'],
  'background': Theme_Colors['DarkBlue_default'],
}

#
# https://docs.qtile.org/en/latest/manual/ref/widgets.html#genpolltext
#
genPollText_GPU_args = {
  'func': get_gpu_usage,
  'update_interval': 5, # seconds

  'padding': 2,
  'fontsize': 16,
  'font': font_set['main'],

  'foreground': Theme_Colors['LightBlue'],
  'background': Theme_Colors['DarkBlue_default'],
}

#
# https://docs.qtile.org/en/latest/manual/ref/widgets.html#memory
#
memory_args = {
  'format': '<small>Mem</small> {MemUsed:.0f}{mm}/{MemTotal:.0f}{mm}',
  # 'format': 'Mem: {MemUsed:.0f}{mm}/{MemTotal:.0f}{mm} Swap: {SwapUsed:.0f}{ms}/{SwapTotal:.0f}{ms}',
  'measure_mem': 'G',
  'update_interval': 2, # seconds ?

  'padding': 2,
  'fontsize': 16,
  'font': font_set['main'],

  'foreground': Theme_Colors['LightBlue'],
  'background': Theme_Colors['DarkBlue_default'],
}

#
# https://docs.qtile.org/en/latest/manual/ref/widgets.html#checkupdates
#
checkUpdates_args = {
  'display_format': '<small>Upd</small> {updates}',
  'update_interval': 600, # seconds
  'distro': 'Arch_checkupdates',

  'no_update_string': '<small>NoUpd</small>',
  'initial_text': '<small>Now checking</small>',

  'padding': 2,
  'fontsize': 14,
  'font': font_set['main'],

  'foreground': Theme_Colors['LightBlue'], # this is initial?
  'colour_have_updates': Theme_Colors['LightBlue'],
  'colour_no_updates': Theme_Colors['LightBlue'],
  'background': Theme_Colors['DarkBlue_default'],
}

#
# https://docs.qtile.org/en/latest/manual/ref/widgets.html#genpolltext
#
genPollText_uptime_args = {
  'func': get_uptime,
  'update_interval': 60, # seconds

  'padding': 2,
  'fontsize': 14,
  'font': font_set['main'],

  'foreground': Theme_Colors['LightBlue'],
  'background': Theme_Colors['DarkBlue_default'],
}

if hostname_chandanna == my_hostname:
  #
  # https://docs.qtile.org/en/latest/manual/ref/widgets.html#pulsevolume
  #
  volume_widget = widget.PulseVolume
  volume_args = {
    'emoji': False,
    'fmt': '<small>Vol</small> {}',
    'mute_format': 'Mute',
    'padding': 2,
    'fontsize': 16,
    'font': font_set['main'],
    'foreground': Theme_Colors['LightBlue'],
    'background': Theme_Colors['DarkBlue_default'],
    'mute_foreground': Theme_Colors['Oreange'],
  }
else:
  #
  # https://docs.qtile.org/en/latest/manual/ref/widgets.html#volume
  #
  volume_widget = widget.Volume
  volume_args = {
    'emoji': False,
    'fmt': 'Vol: {}',
    'mute_format': 'Mute',
    'padding': 4,
    'fontsize': 16,
    'font': font_set['main'],
    'mouse_callbacks': {
      # Button1 is mute on/off
      'Button3': lambda: qtile.spawn('pavucontrol'),
    },
    'foreground': Theme_Colors['LightBlue'],
    'background': Theme_Colors['DarkBlue_default'],
  }

#
# https://docs.qtile.org/en/latest/manual/ref/widgets.html#clock
#
clock_args = {
  'format': '%Y' + '<small>/R' + str(current_gengou_reiwa) + '</small>-%m-%d %a %H:%M',

  'padding': 0,
  'fontsize': 22,
  'font': font_set['main'],

  'foreground': Theme_Colors['Oreange'],
  'background': Theme_Colors['DarkBlue_default'],
}

#
# https://docs.qtile.org/en/latest/manual/ref/widgets.html#systray
#
systray_args = {
  'icon_size': 16,
  'padding': 2,

  'background': Theme_Colors['DarkBlue_default'],
}

#
# https://docs.qtile.org/en/latest/manual/ref/widgets.html#textbox
#
textBox_power_menu_args = {
  'fmt': ' ', # ' ',
  'fontsize': 20,
  'font': font_set['main'],
  'padding': 0,

  'mouse_callbacks': {
    'Button1': lazy.function(show_power_menu),
  },

  'foreground': Theme_Colors['Oreange'],
  'background': Theme_Colors['DarkBlue_default'],
}


##


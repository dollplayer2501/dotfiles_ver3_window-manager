"""
clipmenu
========

cdown/clipmenu: Clipboard management using dmenu
https://github.com/cdown/clipmenu
"""

import subprocess
#
from libqtile import qtile
#
from modules.variables import font_set
from theme_colors import Theme_Colors


#
# TODO: 2026-11-11
#   Include the command to clear all clipboard contents (`clipdel -d '.*'`) in the very first line.
#
# TODO: 2026-11-11
#   Though perhaps not the right place to discuss this:
#     1. Settings for applications that should be excluded from ClipMenu (e.g., password managers).
#        This requires dotfiles.
#     2. Approach for integration with `fzf`.
#
def dmenu_clipmenu_menu(qtile):

  #
  #
  #

  font_setting_font_size = 18
  font_setting = '-'.join([font_set['sub1'], str(font_setting_font_size),])

  #
  # TODO: 2026-11-11
  #   Implement shared, externalized configurations, including those for the power menu.
  #   It seems the only things that can be shared are `-b` and the color scheme.
  #
  dmenu_conf_common = [
    'clipmenu',
    '-b',
    '-fn', font_setting,
    '-nf', Theme_Colors['DarkBlue_default'],
    '-nb', Theme_Colors['Oreange'],
    '-sf', Theme_Colors['Oreange'],
    '-sb', Theme_Colors['DarkBlue_default'],
  ]

  #
  #
  #

  dmenu_conf_clip = dmenu_conf_common + [
    '-p', 'Clip menu!',
  ]

  result = subprocess.run(
    dmenu_conf_clip,
    text = True,
    capture_output = True,
  )

  select_power = result.stdout.strip()


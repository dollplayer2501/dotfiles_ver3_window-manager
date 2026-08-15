"""
Variables
=========

"""

import os
from datetime import datetime
#
# from libqtile.utils import guess_terminal


#
# Keys
#

MOD4 = 'mod4' # Windows key, Super
ALT = 'mod1'
CONTROL = 'control'
SHIFT = 'shift'
TAB = 'Tab'
SPACE = 'space'
RETURN = 'Return'

UP = 'Up'
DOWN = 'Down'
LEFT = 'Left'
RIGHT = 'Right'


#
# Shell scripts
#
# NOTE:
#  The startup and shutdown processes are implemented using shell scripts,
#  but they can also be implemented within hooks.
#

autostart_sh = os.path.expanduser('~/.config/qtile/scripts/autostart.sh')
shutdown_sh = os.path.expanduser('~/.config/qtile/scripts/shutdown.sh')


#
# Fonts
#

font_set = {
  'main': 'Raleway Light',
  'sub1': 'Noto Sans CJK JP Thin',
  'sub2': 'CaskaydiaMono NFM Light',
}


#
# Path
#

default_wallpaper = '/usr/share/endeavouros/backgrounds/endeavouros-wallpaper.png'
custom_layout_icon_path = [
  os.path.expanduser('~/.config/qtile/icons/layout-icons')
]
custom_popup_icon_path = os.path.expanduser('~/.config/qtile/icons/popup-icons')


#
# Japanese era name, `Reiwa` is supported.
#

current_date_time = datetime.now()
current_gengou_reiwa = int(current_date_time.strftime('%Y')) - 2018


#
# Screen, workspace
#

workspace_all = ['1', '2', '3', '4', '5', '7', '8', '9',]
workspace_main = ['1', '2', '3', '4', '5', '9',]
workspace_sub = ['6', '7', '8',] # This does not use


##

"""
Variables
=========

"""

import datetime
import os
import socket

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
# My hostname
#

my_hostname = socket.gethostname().lower()
hostname_chandanna = 'chandanna' # ASRock X600M-STX AMD Ryzen 5 8600G
hostname_bacstual = 'bacstual'   # ThinkPad X13 Gen 1 AMD Ryzen 5 PRO 4650U


#
# Shell scripts
#
# NOTE:
#  The startup and shutdown processes are implemented using shell scripts,
#  but they can also be implemented within hooks.
#

autostart_sh = os.path.expanduser('~/.config/qtile/scripts/autostart..%s.sh' % (my_hostname))
shutdown_sh = os.path.expanduser('~/.config/qtile/scripts/shutdown.sh')
dex_log = os.path.expanduser('~/.local/share/qtile/dex.log')


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

current_date_time = datetime.datetime.now()
current_gengou_reiwa = int(current_date_time.strftime('%Y')) - 2018


#
# Screen, workspace
#

# TODO:
#  Is this unnecessary?
workspace_all = ['1', '2', '3', '4', '5', '6', '7', '8', '9',]
workspace_main = ['1', '2', '3', '4', '5', '9',]
workspace_sub = ['6', '7', '8',] # This does not use


#
#
#

keychord_z_dic = {
  'b': {
    'command': 'firefox',
    'description': 'Run web browser',
  },
  'm': {
    'command': 'thunderbird',
    'description': 'Run mailer',
  },
  'p': {
    'command': 'keepassxc',
    'description': 'Run password manager',
  },
  'f': {
    'command': 'thunar',
    'description': 'Run file explorer',
  },
  'v': {
    'command': 'vlc',
    'description': 'Run video player',
  },

  'g': {
    'command': 'gimp',
    'description': 'Run raster graphic manipulation',
  },
  'i': {
    'command': 'inkscape',
    'description': 'Run vector graphic manipulation',
  },

  'o': {
    'command': 'libreoffice',
    'description': 'Run office suite',
  },
  'n': {
    'command': 'notable',
    'description': 'Run notebook',
  },
  'z': {
    'command': 'mousepad',
    'description': 'Run memo',
  },

  't': {
    'command': 'kitty',
    'description': 'Run terminal',
  },
  's': {
    'command': 'flatpak run com.valvesoftware.Steam',
    'description': 'Run gaming platform',
  },
}

keychord_z_sort = dict(sorted(keychord_z_dic.items()))

keychord_z_str  = '<span font="Monospace" font-size="xx-large">'
keychord_z_str += '<span font-weight="bold">Mod4 + z is...' + '</span>' + "\n\n"
keychord_z_str += "\n".join(f"{k}: {v['description']}, {v['command']}" for k, v in keychord_z_sort.items())
keychord_z_str += '</span>'

#
# TODO: 2026-10-15
#   There ought to be a smarter way to go about this, but for now, I’ll set that aside.
#
keychord_x_str  = '<span font="Monospace" font-size="xx-large">'
keychord_x_str += '<span font-weight="bold">Mod4 + x is...' + '</span>' + "\n"
keychord_x_str += 'q: Logout' + "\n"
keychord_x_str += 'r: Reload the config' + "\n"
keychord_x_str += 'f: Run Font manager' + "\n"
keychord_x_str += 'g: Run Gparted' + "\n"
keychord_x_str += 'x: Run Xfce4 Settings' + "\n"
keychord_x_str += '</span>' + "\n"


##

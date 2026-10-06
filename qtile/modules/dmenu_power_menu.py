#
#
#

import subprocess

from modules.variables import font_set
from theme_colors import Theme_Colors


def dmenu_power_menu(qtile):
  choices = [
    'Screensaver',
    'Logout',
    'Power off',
    'Reboot',
  ]

  font_setting_font_size = 24
  font_setting = '-'.join([font_set['main'], str(font_setting_font_size),])

  result = subprocess.run(
    ['dmenu',
      '-b',                          # Bottom
      '-i',                          # Case-insensitive
      '-p', 'Power menu!',
      '-fn', font_setting,
      # '-l', str(len(choices)),
      '-nf', Theme_Colors['Oreange'],
      '-nb', Theme_Colors['DarkBlue_default'],
      '-sf', Theme_Colors['DarkBlue_default'],
      '-sb', Theme_Colors['Oreange'],
    ],
    input = '\n'.join(choices),
    text = True,
    capture_output = True,
  )

  choice = result.stdout.strip()

  if 'Screensaver' == choice:
    subprocess.run([
      'xfce4-screensaver-command',
      '--activate',
    ])

  elif 'Logout' == choice:
    qtile.cmd_shutdown()

  elif 'Power off' == choice:
    subprocess.run([
      'systemctl',
      'poweroff',
    ])

  elif 'Reboot' == choice:
    subprocess.run([
      'systemctl',
      'reboot',
    ])

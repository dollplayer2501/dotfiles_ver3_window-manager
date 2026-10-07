#
#
#

import subprocess
#
from libqtile import qtile
#
from modules.variables import font_set
from theme_colors import Theme_Colors


def dmenu_power_menu(qtile):
  choices = [
    'Screensaver',
    'Logout',
    'Reload Qtile',
    'Power off',
    'Reboot',
  ]

  font_setting_font_size = 24
  font_setting = '-'.join([font_set['main'], str(font_setting_font_size),])

  result = subprocess.run(
    ['dmenu',
      '-b',
      '-i', # Case-insensitive
      '-p', 'Power menu!',
      '-l', str(len(choices)),
      '-fn', font_setting,
      '-nf', Theme_Colors['DarkBlue_default'],
      '-nb', Theme_Colors['Oreange'],
      '-sf', Theme_Colors['Oreange'],
      '-sb', Theme_Colors['DarkBlue_default'],
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
    qtile.shutdown()

  elif 'Reload Qtile' == choice:
    qtile.reload_config()

  elif 'Power off' == choice:
    # TODO: 2026-10-07
    #   Add dmenu for Yes/No selection
    subprocess.run([
      'systemctl',
      'poweroff',
    ])

  elif 'Reboot' == choice:
    # TODO: 2026-10-07
    #   Add dmenu for Yes/No selection
    subprocess.run([
      'systemctl',
      'reboot',
    ])

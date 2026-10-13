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

  #
  #
  #

  def _func_yes_no(_dmenu_const: list, _prompt: str) -> str:

    choices_yes_no = [
      'No',
      'Yes',
    ]

    dmenu_conf_yes_no = _dmenu_const + [
      '-p', _prompt,
      '-l', str(len(choices_yes_no)),
    ]

    result = subprocess.run(
      dmenu_conf_yes_no,
      input = '\n'.join(choices_yes_no),
      text = True,
      capture_output = True,
    )

    return result.stdout.strip()





  #
  #
  #

  font_setting_font_size = 24
  font_setting = '-'.join([font_set['main'], str(font_setting_font_size),])

  dmenu_conf_common = [
    'dmenu',
    '-b',
    '-i', # Case-insensitive
    '-fn', font_setting,
    '-nf', Theme_Colors['DarkBlue_default'],
    '-nb', Theme_Colors['Oreange'],
    '-sf', Theme_Colors['Oreange'],
    '-sb', Theme_Colors['DarkBlue_default'],
  ]

  #

  choices_power = [
    'Screensaver',
    'Logout',
    'Reload Qtile',
    'Power off',
    'Reboot',
  ]


  #
  #
  #

  dmenu_conf_power = dmenu_conf_common + [
    '-p', 'Power menu!',
    '-l', str(len(choices_power)),
  ]

  result = subprocess.run(
    dmenu_conf_power,
    input = '\n'.join(choices_power),
    text = True,
    capture_output = True,
  )

  select_power = result.stdout.strip()

  #
  #
  #

  if 'Screensaver' == select_power:
    subprocess.run([
      'xfce4-screensaver-command',
      '--activate',
    ])

  elif 'Logout' == select_power:
    qtile.shutdown()

  elif 'Reload Qtile' == select_power:
    qtile.reload_config()

    # subprocess.run([
    #   'notify-send',
    #   '-u', 'low',
    #   '-t', '2',
    #   'Qtile notification!',
    #   'Reload Qtile!'
    # ])

  elif 'Power off' == select_power:
    select_yes_no = _func_yes_no(dmenu_conf_common, 'Power Off?')
    if 'Yes' == select_yes_no:
      subprocess.run([
        'systemctl',
        'poweroff',
      ])

  elif 'Reboot' == select_power:
    select_yes_no = _func_yes_no(dmenu_conf_common, 'Reboot?')
    if 'Yes' == select_yes_no:
      subprocess.run([
        'systemctl',
        'reboot',
      ])

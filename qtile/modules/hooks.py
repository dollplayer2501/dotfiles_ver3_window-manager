"""
Hooks
=====

I don't really understand.
Although it's not directly related to this function, is it possible to write logs at any time?

Hooks - Examples
https://docs.qtile.org/en/stable/manual/config/hooks.html

Built-in Hooks
https://docs.qtile.org/en/stable/manual/ref/hooks.html
"""

import os
import shutil
import subprocess
#
from libqtile import hook, qtile, widget
from libqtile.utils import send_notification # NOTE: need `python-dbus-fast`
from libqtile.log_utils import logger
#
from modules.variables import autostart_sh, shutdown_sh, dex_log, workspace_all, workspace_main, workspace_sub


logger.setLevel('INFO')

groupbox1 = widget.GroupBox(visible_groups = workspace_main)
groupbox2 = widget.GroupBox(visible_groups = workspace_sub)


#
# NOTE:
#
#
# Picom settings
#
#  {
#    match = "QTILE_BAR:32c = 1";
#    opacity = 1.0;
#  },
#
# Qtile settings
#
# @hook.subscribe.startup
# def _():
#   for screen in qtile.screens:
#     for b in (screen.top, screen.bottom, screen.left, screen.right):
#       if b is not None and getattr(b, "window", None) is not None:
#         b.window.window.set_property("QTILE_BAR", 1, "CARDINAL", 32)
#


@hook.subscribe.startup_once
def autostart():
  logger.info('Hook: startup_once! in')

  if os.path.exists(autostart_sh):
    subprocess.call([autostart_sh])

  if shutil.which('dex'):
    logger.info('Hook: dex is alive!')
    with open(dex_log, 'w') as f:
      subprocess.Popen(['dex', '--autostart', '--environment', 'Qtile'],
        stdout = f, stderr = f)

  logger.info('Hook: startup_once! out')


@hook.subscribe.startup_complete
def run_every_startup():
  logger.info('Hook: startup_complete!')


@hook.subscribe.shutdown
def autostart():
  logger.info('Hook: shutdown!')

  if os.path.exists(shutdown_sh):
    subprocess.run([shutdown_sh])


@hook.subscribe.restart
def run_every_startup():
  # NOTE: This does not display?
  logger.info('Hook: restart')


@hook.subscribe.screens_reconfigured
async def _():
  if len(qtile.screens) > 1:
    groupbox1.visible_groups = workspace_main
  else:
    groupbox1.visible_groups = workspace_all
  if hasattr(groupbox1, 'bar'):
    groupbox1.bar.draw()


@hook.subscribe.enter_chord
def enter_chord(chord_name):
  # send_notification("qtile", "Started {chord_name} key chord.")
  pass


# @hook.subscribe.client_new
# def _follow(client):
#   if client.group and client.group.name == "5":
#     client.group.toscreen()


##


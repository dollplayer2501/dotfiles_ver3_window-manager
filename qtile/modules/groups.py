"""
Groups
======

The layout that can be used is set for each workspace.
For layout settings, see `./modules/layouts.py`.

I have a dual monitor setup, but I only use one screen.

https://docs.qtile.org/en/stable/manual/config/groups.html
"""

from libqtile.config import Key, Group, Match
from libqtile.lazy import lazy
from libqtile import layout
#
from modules.variables import MOD4, SHIFT
from modules.keys import keys
from modules.layouts import (
    layout_setting_columns,
    layout_setting_floating,
    layout_setting_matrix,
    layout_setting_max,
    layout_setting_monadTall,
    layout_setting_monadWide,
    layout_setting_treeTab,
    layout_setting_verticalTile,
    # layout_setting_plasma,
  )
from modules.functions import (
    go_to_group,
    go_to_group_and_move_window,
  )


group_defaults = dict(
    init = True,
    persist = True,
  )


groups = [

  Group(screen_affinity = 0, position = 1, name = '1', label = '1.terminal',
    layouts = [
      layout.TreeTab(**layout_setting_treeTab, panel_width = 450),
      layout.VerticalTile(**layout_setting_verticalTile),
      layout.Max(**layout_setting_max),
    ],
    matches = [
      Match(wm_class = 'kitty'),
      Match(wm_class = 'Meld'),
      Match(wm_class = 'Notable'),
    ],
    **group_defaults,
  ),

  Group(screen_affinity = 0, position = 2, name = '2', label = '2.code',
    layouts = [
      layout.Max(**layout_setting_max),
      layout.MonadWide(**layout_setting_monadWide),
      layout.MonadTall(**layout_setting_monadTall),
    ],
    matches = [
      Match(wm_class = 'code-oss'),
    ],
    **group_defaults,
  ),

  Group(screen_affinity = 0, position = 3, name = '3', label = '3.web',
    layouts = [
      layout.TreeTab(**layout_setting_treeTab, panel_width = 350),
      layout.Max(**layout_setting_max),
    ],
    matches = [
      Match(wm_class = 'firefox'),
      Match(wm_class = 'org.mozilla.Thunderbird'),
      Match(wm_class = 'keepassxc'),
    ],
    **group_defaults,
  ),

  Group(screen_affinity = 0, position = 4, name = '4', label = '4.tool',
    layouts = [
      layout.MonadWide(**layout_setting_monadWide),
      layout.Max(**layout_setting_max),
      layout.MonadTall(**layout_setting_monadTall),
      layout.Floating(**layout_setting_floating),
    ],
    matches = [
      Match(wm_class = 'Thunar'),
      Match(wm_class = 'org.gnome.Nautilus'),
    ],
    **group_defaults,
  ),

  Group(screen_affinity = 0, position = 5, name = '5', label = '5.misc',
    layouts = [
      layout.Max(**layout_setting_max),
      layout.TreeTab(**layout_setting_treeTab, panel_width = 350),
      layout.Floating(**layout_setting_floating),
    ],
    matches = [
      # TODO: Is this function not enabled when starting from Thunar?
      Match(wm_class = 'libreoffice-startcenter'),
      Match(wm_class = 'libreoffice-writer'),

      Match(wm_class = 'Gimp'),
      Match(wm_class = 'steam'),
      Match(wm_class = 'Virt-manager'),
      Match(wm_class = 'GParted'),
    ],
    **group_defaults,
  ),

  # Group(screen_affinity = 0, position = 6, name = '6', label = '6.plasma',
  #   layouts = [
  #     layout.Plasma(**layout_setting_plasma),
  #   ],
  #   **group_defaults,
  # ),

  Group(screen_affinity = 0, position = 9,
    name = '9', label = '9.null',
    layouts = [
      layout.Matrix(**layout_setting_matrix, columns = 3),
      layout.Columns(**layout_setting_columns),
      layout.Floating(**layout_setting_floating),
    ],
    **group_defaults,
  ),
]


for i in groups:
  keys.append(
    Key([MOD4], i.name, lazy.function(go_to_group(i.name)),
      desc = 'Switch to group {}'.format(i.name))
  )
  keys.append(
    Key([MOD4, SHIFT], i.name, lazy.function(go_to_group_and_move_window(i.name)),
      desc = 'Switch to & move focused window to group {}'.format(i.name))
  )


##


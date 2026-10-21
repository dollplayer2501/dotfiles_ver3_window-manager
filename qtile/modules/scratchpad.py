"""
ScratchPad and DropDown
=======================
I simply implemented this because the feature exists; I haven't decided yet whether to use it permanently.

https://docs.qtile.org/en/latest/manual/config/groups.html#scratchpad-and-dropdown
"""

from libqtile.config import Key, KeyChord, Group, ScratchPad, DropDown
from libqtile.lazy import lazy

from modules.keys import keys
from modules.groups import groups
from modules.variables import MOD4


groups.append(
  ScratchPad(
    'scratchpad',
    [
      DropDown(
        'term',
        'kitty --class dropdown-kitty',
        width = 0.9,
        height = 0.6,
        x = 0.05,
        y = 0,
        on_focus_lost_hide = False,
        warp_pointer = False,
        opacity = 1.0,
      ),
      DropDown(
        'filer',
        'thunar',
        width = 0.9,
        height = 0.7,
        x = 0.05,
        y = 0,
        on_focus_lost_hide = False,
        warp_pointer = False,
        opacity = 1.0,
      ),
    ]
  )
)

keys.extend([
  Key([MOD4], 'u', lazy.group['scratchpad'].dropdown_toggle('term'), desc = 'Dropdown termiinal'),

  KeyChord([MOD4], 'c', [
      Key([], 't', lazy.group['scratchpad'].dropdown_toggle('term'), desc = 'Dropdown termiinal'),
      Key([], 'f', lazy.group['scratchpad'].dropdown_toggle('filer'), desc = 'Dropdown file explorer'),
    ],
    mode = False,
    name = 'Dropdown',
  ),
])



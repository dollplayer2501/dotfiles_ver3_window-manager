"""
Keys
====

https://docs.qtile.org/en/stable/manual/config/keys.html
"""

from libqtile.lazy import lazy
from libqtile.config import Key, KeyChord
#
from modules.variables import (
  MOD4, CONTROL, SHIFT, TAB, SPACE, RETURN, UP, DOWN, LEFT, RIGHT,
  keychord_z_dic,
  keychord_z_str,
  keychord_x_str,
)
from modules.functions import focus_next_floating, spawn_by_group
from modules.dmenu_power_menu import dmenu_power_menu


keys = [
  # A list of available commands that can be bound to keys can be found
  # at https://docs.qtile.org/en/latest/manual/config/lazy.html


  # Switch between windows
  Key([MOD4], 'h', lazy.layout.left(),  desc = 'Move focus to left'),
  Key([MOD4], 'l', lazy.layout.right(), desc = 'Move focus to right'),
  Key([MOD4], 'j', lazy.layout.down(),  desc = 'Move focus down'),
  Key([MOD4], 'k', lazy.layout.up(),    desc = 'Move focus up'),


  # Move windows between left/right columns or move up/down in current stack.
  # Moving out of range in Columns layout will create new column.

  # NOTE:
  #   .config/qtile · Derek Taylor / Dotfiles · GitLab
  #    https://gitlab.com/dwt1/dotfiles/-/tree/master/.config/qtile?ref_type=heads
  Key([MOD4, SHIFT], 'h',
    lazy.layout.shuffle_left(),
    lazy.layout.move_left().when(layout = ['treetab']),
    desc = 'Move window to the left/move tab left in treetab'),
  Key([MOD4, SHIFT], 'l',
    lazy.layout.shuffle_right(),
    lazy.layout.move_right().when(layout = ['treetab']),
    desc = 'Move window to the right/move tab right in treetab'),
  Key([MOD4, SHIFT], 'j',
    lazy.layout.shuffle_down(),
    lazy.layout.section_down().when(layout = ['treetab']),
    desc = 'Move window down/move down a section in treetab'),
  Key([MOD4, SHIFT], 'k',
    lazy.layout.shuffle_up(),
    lazy.layout.section_up().when(layout = ['treetab']),
    desc = 'Move window up/move up a section in treetab'),


  # Grow windows. If current window is on the edge of screen and direction
  # will be to screen edge - window would shrink.
  Key([MOD4, CONTROL], 'h', lazy.layout.grow_left(),  desc = 'Grow window to left'),
  Key([MOD4, CONTROL], 'l', lazy.layout.grow_right(), desc = 'Grow window to right'),
  Key([MOD4, CONTROL], 'j', lazy.layout.grow_down(),  desc = 'Grow window to down'),
  Key([MOD4, CONTROL], 'k', lazy.layout.grow_up(),    desc = 'Grow window to up'),


  ## Key([mod4, SHIFT, CONTROL], 'h', lazy.layout.swap_column_left(),  desc = 'Swap Column left'),
  ## Key([mod4, SHIFT, CONTROL], 'l', lazy.layout.swap_column_right(), desc = 'Swap Column right'),


  Key([MOD4], UP,    lazy.window.move_floating(0, -10), desc = 'Move floating window to up'),
  Key([MOD4], DOWN,  lazy.window.move_floating(0, 10),  desc = 'Move floating window to down'),
  Key([MOD4], LEFT,  lazy.window.move_floating(-10, 0), desc = 'Move floating window to left'),
  Key([MOD4], RIGHT, lazy.window.move_floating(10, 0),  desc = 'Move floating window to right'),


  Key([MOD4, SHIFT], UP,    lazy.window.resize_floating(0, 10),  desc = 'Resize floating window to bottom, large'),
  Key([MOD4, SHIFT], DOWN,  lazy.window.resize_floating(0, -10), desc = 'Resize floating window to bottom, small'),
  Key([MOD4, SHIFT], LEFT,  lazy.window.resize_floating(-5, 0),  desc = 'Resize floating window to right, small'),
  Key([MOD4, SHIFT], RIGHT, lazy.window.resize_floating(5, 0),   desc = 'Resize floating window to right, large'),


  Key([MOD4], 'n', lazy.layout.normalize(),         desc = 'Reset all window sizes'),
  Key([MOD4], 'm', lazy.layout.maximize(),          desc = 'Maximize window sizes'),
  Key([MOD4], 'f', lazy.window.toggle_fullscreen(), desc = 'Toggle fullscreen on the focused window'),
  Key([MOD4], 't', lazy.window.toggle_floating(),   desc = 'Toggle floating on the focused window'),
  Key([MOD4], 'w', lazy.window.kill(),              desc = 'Kill focused window'),
  Key([MOD4], 'b', lazy.hide_show_bar(position = 'bottom'), desc = 'Toggle bottom bar'),

  # Toggle between split and unsplit sides of stack.
  # Split = all windows displayed
  # Unsplit = 1 window displayed, like Max layout, but still with
  # multiple stack panes
  Key([MOD4, SHIFT], RETURN, lazy.layout.toggle_split(), desc = 'Toggle between split and unsplit sides of stack'),


  Key([MOD4], TAB,    lazy.next_layout(),            desc = 'Toggle between layouts'),
  Key([MOD4], SPACE,  lazy.layout.next(),            desc = 'Move normal window focus to other window'),
  Key([MOD4], RETURN, lazy.function(spawn_by_group), desc = 'Spawn app by group, kitty, firefox, thunar'),
  Key([MOD4, SHIFT], SPACE, lazy.function(focus_next_floating), desc = 'Move floating window focus to other window'),


  Key([MOD4],          'r', lazy.spawncmd(),      desc = 'Spawn a command using a prompt widget'),
  # TODO:
  #  Distinguishing between success and failure when reloading Qtile might be difficult, but should we issue a notification?
  Key([MOD4, CONTROL], 'r', lazy.reload_config(), desc = 'Reload the config'),
  Key([MOD4, CONTROL], 'q', lazy.shutdown(),      desc = 'Logout session'),
  Key([MOD4],          'd', lazy.function(dmenu_power_menu), desc = 'Run power menu'),
  Key([MOD4], 'period',     lazy.next_screen(),   desc = 'Toggle monitor, if 2 monitors'),


  # NOTE:
  #  This is handled by creating a function for the Fish shell.
  #    - dotfiles_ver3_terminal/fish/functions/my_scrot_now.fish at main · dollplayer2501/dotfiles_ver3_terminal
  #      https://github.com/dollplayer2501/dotfiles_ver3_terminal/blob/main/fish/functions/my_scrot_now.fish
  #    - dotfiles_ver3_terminal/fish/functions/my_scrot_wait.fish at main · dollplayer2501/dotfiles_ver3_terminal
  #      https://github.com/dollplayer2501/dotfiles_ver3_terminal/blob/main/fish/functions/my_scrot_wait.fish
  Key([MOD4, CONTROL], 'p', lazy.spawn("fish -c 'my_scrot_now'"),  desc = 'Print screen now'),
  Key([MOD4, CONTROL], 'i', lazy.spawn("fish -c 'my_scrot_wait'"), desc = 'Print screen after 10 sec'),


  KeyChord([MOD4], 'z', [
      # TODO: 2026-10-15
      # Key([SHIFT], 'b', lazy.spawn('firefox --private-window about:blank'), desc = 'Run Firefox, private'),
      # Implementation is possible, but it is not being handled correctly by gen-keybinding-img.

      # TODO: 2026-10-15
      #   Isolate the `keychord` functionality—in other words, move it into a separate file.

      # Web Browser
      Key([], 'b', lazy.spawn(keychord_z_dic['b']['command']), desc = keychord_z_dic['b']['description']),
      # Password Manager
      Key([], 'p', lazy.spawn(keychord_z_dic['p']['command']), desc = keychord_z_dic['p']['description']),
      # Mailer
      Key([], 'm', lazy.spawn(keychord_z_dic['m']['command']), desc = keychord_z_dic['m']['description']),
      # Filer
      Key([], 'f', lazy.spawn(keychord_z_dic['f']['command']), desc = keychord_z_dic['f']['description']),
      # Video
      Key([], 'v', lazy.spawn(keychord_z_dic['v']['command']), desc = keychord_z_dic['v']['description']),
      # Graphic, Raster format
      Key([], 'g', lazy.spawn(keychord_z_dic['g']['command']), desc = keychord_z_dic['g']['description']),
      # Graphic, Vector format
      Key([], 'i', lazy.spawn(keychord_z_dic['i']['command']), desc = keychord_z_dic['i']['description']),
      # Office
      Key([], 'o', lazy.spawn(keychord_z_dic['o']['command']), desc = keychord_z_dic['o']['description']),
      # Terminal
      Key([], 't', lazy.spawn(keychord_z_dic['t']['command']), desc = keychord_z_dic['t']['description']),
      #
      Key([], 'n', lazy.spawn(keychord_z_dic['n']['command']), desc = keychord_z_dic['n']['description']),
      Key([], 's', lazy.spawn(keychord_z_dic['s']['command']), desc = keychord_z_dic['s']['description']),
      Key([], 'z', lazy.spawn(keychord_z_dic['z']['command']), desc = keychord_z_dic['z']['description']),
      #
      Key([], 'h', lazy.spawn(['yad', '--text', keychord_z_str, '--button="OK"', '--fontname="Monospace 20"', ]), desc = 'Help!'),
    ],
    mode = False,
    name = 'Applications',
  ),

  # NOTE:
  #   Just as a trial, for now. It might not be necessary.
  # TODO:
  #   It works as a Qtile feature.
  #   However, it seems that the `Mod4 + Z` and `Mod4 + X` keybindings aren't being captured by `gen-keybinding-img`.
  #   The `KeyChord` bindings shown below are mapped correctly.
  KeyChord([MOD4], 'x', [
      Key([], 'q', lazy.shutdown(),      desc = 'Logout session'),
      Key([], 'r', lazy.reload_config(), desc = 'Reload the config'),
      #
      Key([], 'f', lazy.spawn('font-manager'), desc = 'Run Font manager'),
      Key([], 'g', lazy.spawn('gparted'), desc = 'Run Gparted'),
      Key([], 'x', lazy.spawn('xfce4-settings-manager'), desc = 'Run Xfce4 Settings'),
      #
      Key([], 'h', lazy.spawn(['yad', '--text', keychord_x_str, '--button="OK"', '--fontname="Monospace 20"', ]), desc = 'Help!'),
    ],
    mode = False,
    name = 'System',
  ),
]


##


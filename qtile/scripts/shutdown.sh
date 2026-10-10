#!/usr/bin/sh
#
# shutdown.sh - Script called when Qtile starts
#
# See `@hook.subscribe.shutdown`, `def autostart()` in `./modules/hooks.py`.
#

truncate -s 0 ~/.local/share/qtile/qtile.log
truncate -s 0 ~/.local/share/qtile/dex.log
truncate -s 0 ~/.local/share/picom/picom.log


echo "-- $(hostname) shutdown.sh  out -- " >> ~/.local/share/qtile/qtile.log


##

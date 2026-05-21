#!/usr/bin/sh
#
# autostart.sh - Script called when Qtile starts
#
# See `@hook.subscribe.startup_once`, `def autostart()` in `./modules/hooks.py`.
#

echo '-- autostart.sh in  -- ' >>~/.local/share/qtile/qtile.log

#
# Xfce4
# - /etc/xdg/autostart/
# - ~/.config/autostart/
# - /etc/xdg/xfce4/xinitrc
#


# Xfce Settings Daemon
#   xfsettingsd.desktop
/usr/bin/xfsettingsd --daemon &


# xfce4-power-manager.desktop
#   Power Manager
/usr/bin/xfce4-power-manager --daemon &

# Screensaver
#   xscreensaver.desktop
/usr/bin/xfce4-screensaver &

# blueman, bluez
#  bluetooth.service
## /usr/bin/blueman-applet &


# AT-SPI D-Bus Bus
#   at-spi-dbus-bus.desktop
/usr/lib/at-spi-bus-launcher --launch-immediately &

# xfce-polkit-gnome-authentication-agent-1.desktop
#   PolicyKit Authentication Agent
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &


# xfce4-notifyd.desktop
#  Xfce Notification Daemon
#    command line is `notify-send "abc"`
#    class is "Xfce4-notifyd"
# NOTE: need `python-dbus-fast`
sh -c "systemctl --user start xfce4-notifyd.service 2>/dev/null || exec /usr/lib/xfce4/notifyd/xfce4-notifyd" &

# xapp-sn-watcher.desktop
#  A service that provides the org.kde.StatusNotifierWatcher interface for XApps
/usr/lib/xapps/xapp-sn-watcher &

# user-dirs-update-gtk.desktop
#  User folders update
/usr/bin/xdg-user-dirs-gtk-update &

# nm-applet.desktop
#  NetworkManager Applet
/usr/bin/nm-applet &


#
#
#

# xsetroot -cursor_name left_ptr & disowm

# disable screen-saver
## xset s off

# enable DPMS
## xset +dpms
## xset dpms 1800 1800 1800

# enable screen-lock
## xss-lock -- i3lock -n &

# enable fcitx5
/usr/bin/fcitx5 -d &

# enable Picom
/usr/bin/picom --daemon &


# Mouse cursor speed, only this environment?
# id=$(xinput list --id-only "ELECOM ELECOM BlueLED Mouse")
# xinput --set-prop "$id" "libinput Accel Speed" -0.4

# xinput --set-prop 12 "libinput Accel Profile Enabled" 0 1
# xinput --set-prop 12 "libinput Accel Speed" -0.3

echo '-- autostart.sh out -- ' >>~/.local/share/qtile/qtile.log





# dbus-update-activation-environment $systemd_arg \
#   DESKTOP_SESSION \
#   XAUTHLOCALHOSTNAME=$XAUTHLOCALHOSTNAME \
#   XDG_CACHE_HOME \
#   XDG_CONFIG_DIRS \
#   XDG_CONFIG_HOME \
#   XDG_CURRENT_DESKTOP \
#   XDG_DATA_DIRS \
#   XDG_DATA_HOME \
#   XDG_MENU_PREFIX \
#   XDG_RUNTIME_DIR \
#   XDG_SEAT \
#   XDG_SEAT_PATH \
#   XDG_SESSION_CLASS \
#   XDG_SESSION_DESKTOP \
#   XDG_SESSION_ID \
#   XDG_SESSION_PATH \
#   XDG_SESSION_TYPE \
#   XDG_STATE_HOME



##

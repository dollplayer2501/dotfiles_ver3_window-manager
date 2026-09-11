# Regarding the Window Manager icon in LightDM

First, check which display manager you are using.

`systemctl status display-manager`

**The following assumes the use of LightDM.**
Furthermore, since I use EndeavourOS, this assumes the use of *endeavouros/eos-lightdm-slick-theme*.


Checking which theme is being used.
This output is difficult for me to understand.

`lightdm --show-config`

After various twists and turns, place a 22x22 PNG or SVG file below.

`/usr/share/slick-greeter/badges/qtile-my-local.png`

After various twists and turns, I added the startup session definition shown below.
In practice, it is no different from a standard Qtile setup.

`/usr/share/xsessions/qtile-my-local.desktop`

Presumably, the launch session name (in my case, "qtile-my-local") and the PNG/SVG image name must be identical.
My intention was to use a filename different from the official one—taking into account factors such as the need to check for differences—in anticipation of future updates to these files.

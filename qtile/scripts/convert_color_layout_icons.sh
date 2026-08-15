#!/usr/bin/bash

# NOTE: Purpose of this script:
# To change the color of the default layout icons used by `libqtile.widget.CurrentLayout`.
# Qtile provides its own layout icons.
# However, these files are transparent PNGs with white lines.
# This script converts the white lines to a specified color.
# Alternative approaches could also be considered at this stage.

# NOTE: This path may vary depending on the usage environment.
# NOTE: As a side note, `logo.png` exists in `/usr/lib/pythonX.XX/site-packages/libqtile/resources/`.
DIR_EXT=" /usr/lib/python3.14/site-packages/libqtile/resources/layout-icons/*.png"
# NOTE: With this script, the path is completely deleted and then recreated from scratch.
PATH_OUTPUT="${HOME}/.config/qtile/icons/layout-icons/"

if [ ! -d ${PATH_OUTPUT} ]; then
  mkdir ${PATH_OUTPUT}
else
  rm -rf ${PATH_OUTPUT}
  mkdir  ${PATH_OUTPUT}
fi

for file_path in $(eval echo $DIR_EXT); do
  echo $file_path
  file_name=$(basename "$file_path")
  # echo $file_name

  # NOTE: The color conversion for `layout-spiral.png` is not performed with the ImageMagick arguments below.
  # magick $file_path -fuzz 10% -fill "#FF7F7F" -opaque "#ffffff" ${PATH_OUTPUT}$file_name
  magick "$file_path" -fill "#FF7F7F" -colorize 100% "${PATH_OUTPUT}$file_name"
done

# 'LightBlue':        '#7FBAFF',
# 'Purple':           '#7F3FBF',
# 'Oreange':          '#FF7F7F',
# 'Red':              '#CC3980',


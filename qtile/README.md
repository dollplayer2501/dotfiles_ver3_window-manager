# Qtile configration


<img src="../Chandanna_EndeavourOS_Qtile_2026-05-21_13-26-45.png" width="500">


## Overview

1. **After installing the Xfce4 environment on EndeavourOS, I set up Qtile** and have been using it full-time.  
    In other words, I am making full use of the Xfce4-related infrastructure.
1. **Not** Using [qtile-extras](https://qtile-extras.readthedocs.io/en/stable/).  
    To be precise, I stopped using this.
1. Using Vanilla [dmenu](https://tools.suckless.org/dmenu/), [dex](https://man.archlinux.org/man/extra/dex/dex.1.en).
1. using `scrot` to take screenshots, but I call a Fish shell function that I created, [my_scrot_now](https://github.com/dollplayer2501/dotfiles_ver3_terminal/blob/main/fish/functions/my_scrot_now.fish) and [my_scrot_wait](https://github.com/dollplayer2501/dotfiles_ver3_terminal/blob/main/fish/functions/my_scrot_wait.fish).
1. It's imperfect, but I'm using a modified version of [gen-keybinding-img](https://docs.qtile.org/en/latest/manual/commands/keybindings.html).
1. Notification-related functionality depends on the Xfce4 environment.
1. Using [Raleway font](https://fonts.google.com/specimen/Raleway).
1. As a Japanese person living in Japan, I use the Japanese calendar format.  
    The `Western year/R+number` setting in `widget.Clock` corresponds to this.
1. There might also be "something" that no one other than myself could use immediately.


Notes of special interest follow below.

- [01. Workspaces and layouts](./docs/01.workspaces_and_layouts.md)
- [02. keybinds in images](./docs/02.keybinds_in_images.md)


## TODO:

- [x] Complete separation of `scripts/autostart.sh`  
    `scripts/autostart..chandanna.sh` and `scripts/autostart..bacstual.sh`
- [x] Revised the description so that it does not assume the use of multiple monitors.  
    And Rename `modules/screenbar_*.py` to `built_in_widgets.py` ?  
    **This as concluded for the time being.**
- [x] Separating the configuration and placement of built-in widgets (to avoid lengthy code)  
    **For some reason—though I haven't investigated why—the GPU load isn't displayed on the ASRock X600M-STX.**
- [x] Long-term goal: Implement a shutdown menu (or similar) using dmenu or Rofi.  
    Decided not to use the Popup Toolkit from qtile-extras.
    - Adoption of dmenu
    - Likely not currently using qtile-extras.
- [x] In connection with the above, I am re-examining whether it is necessary to use qtile-extras.
    - Likely not currently using qtile-extras.
- [ ] The possibility of using dmenu in situations requiring Yes/No selections or similar choices.
- [ ] It’s a pretty heavy coding task for me, but... should I revisit `gen-keybinding-img`?
- [ ] Use the `dex` command to manage the contents of `script/autostart.sh` via `~/.config/autostart`.
- [ ] I want to handle notifications entirely using `widget.Notify`, but—compounded by Xfce4-related specifications—it is beyond my current skill level.



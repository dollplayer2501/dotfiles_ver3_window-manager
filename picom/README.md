# My Picom's configuration.

- Instead of following the previous writing style, I rewrote it according to the current writing rules.
- I separated the transparency rules, mainly, into a separate file by adding `@include "my_rules.conf"`.
- Basically, only transparency is used, although some fade settings are also used.
- In my case, I launch Picom from the Qtile window manager, not through `autostart`.
- As mentioned above, specifically, the execution of `/usr/bin/picom --daemon &`

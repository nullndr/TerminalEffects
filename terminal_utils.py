#!/usr/bin/env python

## Font attributes ##
OFF = '\x1b[0m'
DEF_FOREGROUND = '\x1b[39m'
DEF_BACKGROUND = '\x1b[49m'

# effects
BOLD = '\x1b[1m'
FAINT = '\x1b[2m'
ITALIC = '\x1b[3m'
UNDERLINED = '\x1b[4m'
BLINK = '\x1b[5m'
RAPID_BLINK = '\x1b[6m'
SWAP_COLORS = '\x1b[7m'
HIDDEN = '\x1b[8m'
DELETED = '\x1b[9m'
DEF_FONT = '\x1b[10m'
NO_BOLD = '\x1b[21m'
NO_FAINT = '\x1b[22m'
NO_ITALIC = '\x1b[23m'
NO_UNDERLINED = '\x1b[24m'
NO_BLINK = '\x1b[25m'
NO_REVERSE = '\x1b[27m'
REVEAL = '\x1b[28m'

# foreground colors
BLACK = '\x1b[30m'
RED = '\x1b[31m'
GREEN = '\x1b[32m'
YELLOW = '\x1b[33m'
BLUE = '\x1b[34m'
MAGENTA = '\x1b[35m'
CYAN = '\x1b[36m'
WHITE = '\x1b[37m'
TEAL = '\x1b[90m'

# background colors
BACKGROUND_BLACK = '\x1b[40m'
BACKGROUND_RED = '\x1b[41m'
BACKGROUND_GREEN = '\x1b[42m'
BACKGROUND_YELLOW = '\x1b[43m'
BACKGROUND_BLUE = '\x1b[44m'
BACKGROUND_MAGENTA = '\x1b[45m'
BACKGROUND_CYAN = '\x1b[46m'
BACKGROUND_WHITE = '\x1b[47m'
BACKGROUND_TEAL = '\x1b[100m'

# light colors
LIGHT_RED = '\x1b[91m'
LIGHT_GREEN = '\x1b[92m'
LIGHT_YELLOW = '\x1b[93m'
LIGHT_BLUE = '\x1b[94m'
LIGHT_MAGENTA = '\x1b[95m'
LIGHT_CYAN = '\x1b[96m'

# light background colors
BACKGROUND_LIGHT_RED = '\x1b[101m'
BACKGROUND_LIGHT_GREEN = '\x1b[102m'
BACKGROUND_LIGHT_YELLOW = '\x1b[103m'
BACKGROUND_LIGHT_BLUE = '\x1b[104m'
BACKGROUND_LIGHT_MAGENTA = '\x1b[105m'
BACKGROUND_LIGHT_CYAN = '\x1b[106m'

## 256 colors ##
# \x1b[38;5;#m foreground, # = 0 - 255
# \x1b[48;5;#m background, # = 0 - 255
## True Color ##
# \x1b[38;2;r;g;bm r = red, g = green, b = blue foreground
# \x1b[48;2;r;g;bm r = red, g = green, b = blue background

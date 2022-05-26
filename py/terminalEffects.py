#!/usr/bin/env python

## font attributes
OFF = '\x1b[0m'
DEF_FONT = '\x1b[10m'
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

NO_BOLD = '\x1b[21m'
NO_FAINT = '\x1b[22m'
NO_ITALIC = '\x1b[23m'
NO_UNDERLINED = '\x1b[24m'
NO_BLINK = '\x1b[25m'
NO_REVERSE = '\x1b[27m'
NO_HIDDEN = '\x1b[28m'
NO_DELETED = '\x1b[29m'

# foreground colors
BLACK = '\x1b[30m'
RED = '\x1b[31m'
GREEN = '\x1b[32m'
YELLOW = '\x1b[33m'
BLUE = '\x1b[34m'
MAGENTA = '\x1b[35m'
CYAN = '\x1b[36m'
WHITE = '\x1b[37m'

# background colors
BACKGROUND_BLACK = '\x1b[40m'
BACKGROUND_RED = '\x1b[41m'
BACKGROUND_GREEN = '\x1b[42m'
BACKGROUND_YELLOW = '\x1b[43m'
BACKGROUND_BLUE = '\x1b[44m'
BACKGROUND_MAGENTA = '\x1b[45m'
BACKGROUND_CYAN = '\x1b[46m'
BACKGROUND_WHITE = '\x1b[47m'

# light colors
LIGHT_BLACK = '\x1b[90m'
LIGHT_RED = '\x1b[91m'
LIGHT_GREEN = '\x1b[92m'
LIGHT_YELLOW = '\x1b[93m'
LIGHT_BLUE = '\x1b[94m'
LIGHT_MAGENTA = '\x1b[95m'
LIGHT_CYAN = '\x1b[96m'
LIGHT_WHITE = '\x1b[97m'

# light background colors
BACKGROUND_LIGHT_BLACK = '\x1b[100m'
BACKGROUND_LIGHT_RED = '\x1b[101m'
BACKGROUND_LIGHT_GREEN = '\x1b[102m'
BACKGROUND_LIGHT_YELLOW = '\x1b[103m'
BACKGROUND_LIGHT_BLUE = '\x1b[104m'
BACKGROUND_LIGHT_MAGENTA = '\x1b[105m'
BACKGROUND_LIGHT_CYAN = '\x1b[106m'
BACKGROUND_LIGHT_WHITE = '\x1b[107m'

def bold(string: str) -> str:
  return f"{BOLD}{string}{NO_BOLD}"

def faint(string: str) -> str:
  return f"{FAINT}{string}{NO_FAINT}"

def italic(string: str) -> str:
  return f"{ITALIC}{string}{NO_ITALIC}"

def underlined(string: str) -> str:
  return f"{UNDERLINED}{string}{NO_UNDERLINED}"

def blink(string: str) -> str:
  return f"{BLINK}{string}{NO_BLINK}"

def rapidBlink(string: str) -> str:
  return f"{RAPID_BLINK}{string}{NO_BLINK}"

def swapColors(string: str) -> str:
  return f"{SWAP_COLORS}{string}{NO_REVERSE}"

def hidden(string: str) -> str:
  return f"{HIDDEN}{string}{NO_HIDDEN}"

def deleted(string: str) -> str:
  return f"{DELETED}{string}{NO_DELETED}"

def black(string: str) -> str:
  return f"{BLACK}{string}{DEF_FOREGROUND}"

def red(string: str) -> str:
  return f"{RED}{string}{DEF_FOREGROUND}"

def green(string: str) -> str:
  return f"{GREEN}{string}{DEF_FOREGROUND}"

def yellow(string: str) -> str:
  return f"{YELLOW}{string}{DEF_FOREGROUND}"

def blue(string: str) -> str:
  return f"{BLUE}{string}{DEF_FOREGROUND}"

def magenta(string: str) -> str:
  return f"{MAGENTA}{string}{DEF_FOREGROUND}"

def cyan(string: str) -> str:
  return f"{CYAN}{string}{DEF_FOREGROUND}"

def white(string: str) -> str:
  return f"{WHITE}{string}{DEF_FOREGROUND}"

def foreground256(string: str, x: int) -> str:
  return f"\x1b[38;5;{x}m{string}{DEF_FOREGROUND}"

def foregroundRGB(string: str, r: int, g: int, b: int) -> str:
  return f"\x1b[38;2;{r};{g};{b}m{string}{DEF_FOREGROUND}"

def bgBlack(string: str) -> str:
  return f"{BACKGROUND_BLACK}{string}{DEF_BACKGROUND}"

def bgRed(string: str) -> str:
  return f"{BACKGROUND_RED}{string}{DEF_BACKGROUND}"

def bgGreen(string: str) -> str:
  return f"{BACKGROUND_GREEN}{string}{DEF_BACKGROUND}"

def bgYellow(string: str) -> str:
  return f"{BACKGROUND_YELLOW}{string}{DEF_BACKGROUND}"

def bgBlue(string: str) -> str:
  return f"{BACKGROUND_BLUE}{string}{DEF_BACKGROUND}"

def bgMagenta(string: str) -> str:
  return f"{BACKGROUND_MAGENTA}{string}{DEF_BACKGROUND}"

def bgCyan(string: str) -> str:
  return f"{BACKGROUND_CYAN}{string}{DEF_BACKGROUND}"

def bgWhite(string: str) -> str:
  return f"{BACKGROUND_WHITE}{string}{DEF_BACKGROUND}"

def background256(string: str, x: int) -> str:
  return f"\x1b[48;5;{x}m{string}{DEF_BACKGROUND}"

def backgroundRGB(string: str, r: int, g: int, b: int) -> str:
  return f"\x1b[48;2;{r};{g};{b}m{string}{DEF_BACKGROUND}"

def lightBlack(string: str) -> str:
  return f"{LIGHT_BLACK}{string}{DEF_FOREGROUND}"

def lightRed(string: str) -> str:
  return f"{LIGHT_RED}{string}{DEF_FOREGROUND}"

def lightGreen(string: str) -> str:
  return f"{LIGHT_GREEN}{string}{DEF_FOREGROUND}"

def lightYellow(string: str) -> str:
  return f"{LIGHT_YELLOW}{string}{DEF_FOREGROUND}"

def lightBlue(string: str) -> str:
  return f"{LIGHT_BLUE}{string}{DEF_FOREGROUND}"

def lightMagenta(string: str) -> str:
  return f"{LIGHT_MAGENTA}{string}{DEF_FOREGROUND}"

def lightCyan(string: str) -> str:
  return f"{LIGHT_CYAN}{string}{DEF_FOREGROUND}"

def lightWhite(string: str) -> str:
  return f"{LIGHT_WHITE}{string}{DEF_FOREGROUND}"

def bgLightBlack(string: str) -> str:
  return f"{BACKGROUND_LIGHT_BLACK}{string}{DEF_BACKGROUND}"

def bgLightRed(string: str) -> str:
  return f"{BACKGROUND_LIGHT_RED}{string}{DEF_BACKGROUND}"

def bgLightGreen(string: str) -> str:
  return f"{BACKGROUND_GREEN}{string}{DEF_BACKGROUND}"

def bgLightYellow(string: str) -> str:
  return f"{BACKGROUND_YELLOW}{string}{DEF_BACKGROUND}"

def bgLightBlue(string: str) -> str:
  return f"{BACKGROUND_BLUE}{string}{DEF_BACKGROUND}"

def bgLightMagenta(string: str) -> str:
  return f"{BACKGROUND_MAGENTA}{string}{DEF_BACKGROUND}"

def bgLightCyan(string: str) -> str:
  return f"{BACKGROUND_CYAN}{string}{DEF_BACKGROUND}"

def bgLightWhite(string: str) -> str:
  return f"{BACKGROUND_WHITE}{string}{DEF_BACKGROUND}"

#!/usr/bin/env sh

## font attributes
OFF='\x1b[0m'
DEF_FONT='\x1b[10m'
DEF_FOREGROUND='\x1b[39m'
DEF_BACKGROUND='\x1b[49m'

# effects
BOLD='\x1b[1m'
FAINT='\x1b[2m'
ITALIC='\x1b[3m'
UNDERLINED='\x1b[4m'
BLINK='\x1b[5m'
RAPID_BLINK='\x1b[6m'
SWAP_COLORS='\x1b[7m'
HIDDEN='\x1b[8m'
DELETED='\x1b[9m'

NO_BOLD='\x1b[21m'
NO_FAINT='\x1b[22m'
NO_ITALIC='\x1b[23m'
NO_UNDERLINED='\x1b[24m'
NO_BLINK='\x1b[25m'
NO_REVERSE='\x1b[27m'
NO_HIDDEN='\x1b[28m'
NO_DELETED='\x1b[29m'

# foreground colors
BLACK='\x1b[30m'
RED='\x1b[31m'
GREEN='\x1b[32m'
YELLOW='\x1b[33m'
BLUE='\x1b[34m'
MAGENTA='\x1b[35m'
CYAN='\x1b[36m'
WHITE='\x1b[37m'

# background colors
BACKGROUND_BLACK='\x1b[40m'
BACKGROUND_RED='\x1b[41m'
BACKGROUND_GREEN='\x1b[42m'
BACKGROUND_YELLOW='\x1b[43m'
BACKGROUND_BLUE='\x1b[44m'
BACKGROUND_MAGENTA='\x1b[45m'
BACKGROUND_CYAN='\x1b[46m'
BACKGROUND_WHITE='\x1b[47m'

# light colors
LIGHT_BLACK='\x1b[90m'
LIGHT_RED='\x1b[91m'
LIGHT_GREEN='\x1b[92m'
LIGHT_YELLOW='\x1b[93m'
LIGHT_BLUE='\x1b[94m'
LIGHT_MAGENTA='\x1b[95m'
LIGHT_CYAN='\x1b[96m'
LIGHT_WHITE='\x1b[97m'

# light background colors
BACKGROUND_LIGHT_BLACK='\x1b[100m'
BACKGROUND_LIGHT_RED='\x1b[101m'
BACKGROUND_LIGHT_GREEN='\x1b[102m'
BACKGROUND_LIGHT_YELLOW='\x1b[103m'
BACKGROUND_LIGHT_BLUE='\x1b[104m'
BACKGROUND_LIGHT_MAGENTA='\x1b[105m'
BACKGROUND_LIGHT_CYAN='\x1b[106m'
BACKGROUND_LIGHT_WHITE='\x1b[107m'

bold() {
  echo "${BOLD}$1${NO_BOLD}"
}

faint() {
  echo "${FAINT}$1${NO_FAINT}"
}

italic() {
  echo "${ITALIC}$1${NO_ITALIC}" 
}

underlined() {
  echo "${UNDERLINED}$1${NO_UNDERLINED}" 
}

blink() {
  echo "${BLINK}$1${NO_BLINK}" 
}

rapidBlink() {
  echo "${RAPID_BLINK}$1${NO_BLINK}" 
}

swapColors() {
  echo "${SWAP_COLORS}$1${NO_REVERSE}" 
}

hidden() {
  echo "${HIDDEN}$1${NO_HIDDEN}" 
}

deleted() {
  echo "${DELETED}$1${NO_DELETED}" 
}

black() {
  echo "${BLACK}$1${DEF_FOREGROUND}" 
}

red() {
  echo "${RED}$1${DEF_FOREGROUND}" 
}

green() {
  echo "${GREEN}$1${DEF_FOREGROUND}" 
}

yellow() {
  echo "${YELLOW}$1${DEF_FOREGROUND}" 
}

blue() {
  echo "${BLUE}$1${DEF_FOREGROUND}" 
}

magenta() {
  echo "${MAGENTA}$1${DEF_FOREGROUND}" 
}

cyan() {
  echo "${CYAN}$1${DEF_FOREGROUND}" 
}

white() {
  echo "${WHITE}$1${DEF_FOREGROUND}" 
}

foreground256() {
  echo "\x1b[38;5;$2m$1${DEF_FOREGROUND}" 
}

foregroundRGB() {
  echo "\x1b[38;2;$2;$3;$4m$1${DEF_FOREGROUND}" 
}

bgBlack() {
  echo "${BACKGROUND_BLACK}$1${DEF_BACKGROUND}" 
}

bgRed() {
  echo "${BACKGROUND_RED}$1${DEF_BACKGROUND}" 
}

bgGreen() {
  echo "${BACKGROUND_GREEN}$1${DEF_BACKGROUND}" 
}

bgYellow() {
  echo "${BACKGROUND_YELLOW}$1${DEF_BACKGROUND}" 
}

bgBlue() {
  echo "${BACKGROUND_BLUE}$1${DEF_BACKGROUND}" 
}

bgMagenta() {
  echo "${BACKGROUND_MAGENTA}$1${DEF_BACKGROUND}" 
}

bgCyan() {
  echo "${BACKGROUND_CYAN}$1${DEF_BACKGROUND}" 
}

bgWhite() {
  echo "${BACKGROUND_WHITE}$1${DEF_BACKGROUND}" 
}

background256() {
  echo "\x1b[48;5;$2m$1${DEF_BACKGROUND}" 
}

backgroundRGB() {
  echo "\x1b[48;2;$2;$3;$4m$1${DEF_BACKGROUND}" 
}

lightBlack() {
  echo "${LIGHT_BLACK}$1${DEF_FOREGROUND}" 
}

lightRed() {
  echo "${LIGHT_RED}$1${DEF_FOREGROUND}" 
}

lightGreen() {
  echo "${LIGHT_GREEN}$1${DEF_FOREGROUND}" 
}

lightYellow() {
  echo "${LIGHT_YELLOW}$1${DEF_FOREGROUND}" 
}

lightBlue() {
  echo "${LIGHT_BLUE}$1${DEF_FOREGROUND}" 
}

lightMagenta() {
  echo "${LIGHT_MAGENTA}$1${DEF_FOREGROUND}" 
}

lightCyan() {
  echo "${LIGHT_CYAN}$1${DEF_FOREGROUND}" 
}

lightWhite() {
  echo "${LIGHT_WHITE}$1${DEF_FOREGROUND}" 
}

bgLightBlack() {
  echo "${BACKGROUND_LIGHT_BLACK}$1${DEF_BACKGROUND}" 
}

bgLightRed() {
  echo "${BACKGROUND_LIGHT_RED}$1${DEF_BACKGROUND}" 
}

bgLightGreen() {
  echo "${BACKGROUND_GREEN}$1${DEF_BACKGROUND}" 
}

bgLightYellow() {
  echo "${BACKGROUND_YELLOW}$1${DEF_BACKGROUND}" 
}

bgLightBlue() {
  echo "${BACKGROUND_BLUE}$1${DEF_BACKGROUND}" 
}

bgLightMagenta() {
  echo "${BACKGROUND_MAGENTA}$1${DEF_BACKGROUND}" 
}

bgLightCyan() {
  echo "${BACKGROUND_CYAN}$1${DEF_BACKGROUND}" 
}

bgLightWhite() {
  echo "${BACKGROUND_WHITE}$1${DEF_BACKGROUND}"
}
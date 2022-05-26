// font attributes
export const OFF = "\x1b[0m";
export const DEF_FONT = "\x1b[10m";
export const DEF_FOREGROUND = "\x1b[39m";
export const DEF_BACKGROUND = "\x1b[49m";

// effects
export const BOLD = "\x1b[1m";
export const FAINT = "\x1b[2m";
export const ITALIC = "\x1b[3m";
export const UNDERLINED = "\x1b[4m";
export const BLINK = "\x1b[5m";
export const RAPID_BLINK = "\x1b[6m";
export const SWAP_COLORS = "\x1b[7m";
export const HIDDEN = "\x1b[8m";
export const DELETED = "\x1b[9m";

export const NO_BOLD = "\x1b[21m";
export const NO_FAINT = "\x1b[22m";
export const NO_ITALIC = "\x1b[23m";
export const NO_UNDERLINED = "\x1b[24m";
export const NO_BLINK = "\x1b[25m";
export const NO_REVERSE = "\x1b[27m";
export const NO_HIDDEN = "\x1b[28m";
export const NO_DELETED = "\x1b[29m";

// foreground colors
export const BLACK = "\x1b[30m";
export const RED = "\x1b[31m";
export const GREEN = "\x1b[32m";
export const YELLOW = "\x1b[33m";
export const BLUE = "\x1b[34m";
export const MAGENTA = "\x1b[35m";
export const CYAN = "\x1b[36m";
export const WHITE = "\x1b[37m";

// background colors
export const BACKGROUND_BLACK = "\x1b[40m";
export const BACKGROUND_RED = "\x1b[41m";
export const BACKGROUND_GREEN = "\x1b[42m";
export const BACKGROUND_YELLOW = "\x1b[43m";
export const BACKGROUND_BLUE = "\x1b[44m";
export const BACKGROUND_MAGENTA = "\x1b[45m";
export const BACKGROUND_CYAN = "\x1b[46m";
export const BACKGROUND_WHITE = "\x1b[47m";

// light colors
export const LIGHT_BLACK = "\x1b[90m";
export const LIGHT_RED = "\x1b[91m";
export const LIGHT_GREEN = "\x1b[92m";
export const LIGHT_YELLOW = "\x1b[93m";
export const LIGHT_BLUE = "\x1b[94m";
export const LIGHT_MAGENTA = "\x1b[95m";
export const LIGHT_CYAN = "\x1b[96m";
export const LIGHT_WHITE = "\x1b[97m";

// light background colors
export const BACKGROUND_LIGHT_BLACK = "\x1b[100m";
export const BACKGROUND_LIGHT_RED = "\x1b[101m";
export const BACKGROUND_LIGHT_GREEN = "\x1b[102m";
export const BACKGROUND_LIGHT_YELLOW = "\x1b[103m";
export const BACKGROUND_LIGHT_BLUE = "\x1b[104m";
export const BACKGROUND_LIGHT_MAGENTA = "\x1b[105m";
export const BACKGROUND_LIGHT_CYAN = "\x1b[106m";
export const BACKGROUND_LIGHT_WHITE = "\x1b[107m";

export const bold = (string) => `${BOLD}${string}${NO_BOLD}`;

export const faint = (string) => `${FAINT}${string}${NO_FAINT}`;

export const italic = (string) => `${ITALIC}${string}${NO_ITALIC}`;

export const underlined = (string) => `${UNDERLINED}${string}${NO_UNDERLINED}`;

export const blink = (string) => `${BLINK}${string}${NO_BLINK}`;

export const rapidBlink = (string) => `${RAPID_BLINK}${string}${NO_BLINK}`;

export const swapColors = (string) => `${SWAP_COLORS}${string}${NO_REVERSE}`;

export const hidden = (string) => `${HIDDEN}${string}${NO_HIDDEN}`;

export const deleted = (string) => `${DELETED}${string}${NO_DELETED}`;

export const black = (string) => `${BLACK}${string}${DEF_FOREGROUND}`;

export const red = (string) => `${RED}${string}${DEF_FOREGROUND}`;

export const green = (string) => `${GREEN}${string}${DEF_FOREGROUND}`;

export const yellow = (string) => `${YELLOW}${string}${DEF_FOREGROUND}`;

export const blue = (string) => `${BLUE}${string}${DEF_FOREGROUND}`;

export const magenta = (string) => `${MAGENTA}${string}${DEF_FOREGROUND}`;

export const cyan = (string) => `${CYAN}${string}${DEF_FOREGROUND}`;

export const white = (string) => `${WHITE}${string}${DEF_FOREGROUND}`;

export const foreground256 = (string, x) =>
  `\x1b[38;5;${x}m${string}${DEF_FOREGROUND}`;

export const foregroundRGB = (string, r, g, b) =>
  `\x1b[38;2;${r};${g};${b}m${string}${DEF_FOREGROUND}`;

export const bgBlack = (string) =>
  `${BACKGROUND_BLACK}${string}${DEF_BACKGROUND}`;

export const bgRed = (string) => `${BACKGROUND_RED}${string}${DEF_BACKGROUND}`;

export const bgGreen = (string) =>
  `${BACKGROUND_GREEN}${string}${DEF_BACKGROUND}`;

export const bgYellow = (string) =>
  `${BACKGROUND_YELLOW}${string}${DEF_BACKGROUND}`;

export const bgBlue = (string) =>
  `${BACKGROUND_BLUE}${string}${DEF_BACKGROUND}`;

export const bgMagenta = (string) =>
  `${BACKGROUND_MAGENTA}${string}${DEF_BACKGROUND}`;

export const bgCyan = (string) =>
  `${BACKGROUND_CYAN}${string}${DEF_BACKGROUND}`;

export const bgWhite = (string) =>
  `${BACKGROUND_WHITE}${string}${DEF_BACKGROUND}`;

export const background256 = (string, x) =>
  `\x1b[48;5;${x}m${string}${DEF_BACKGROUND}`;

export const backgroundRGB = (string, r, g, b) =>
  `\x1b[48;2;${r};${g};${b}m${string}${DEF_BACKGROUND}`;

export const lightBlack = (string) =>
  `${LIGHT_BLACK}${string}${DEF_FOREGROUND}`;

export const lightRed = (string) => `${LIGHT_RED}${string}${DEF_FOREGROUND}`;

export const lightGreen = (string) =>
  `${LIGHT_GREEN}${string}${DEF_FOREGROUND}`;

export const lightYellow = (string) =>
  `${LIGHT_YELLOW}${string}${DEF_FOREGROUND}`;

export const lightBlue = (string) => `${LIGHT_BLUE}${string}${DEF_FOREGROUND}`;

export const lightMagenta = (string) =>
  `${LIGHT_MAGENTA}${string}${DEF_FOREGROUND}`;

export const lightCyan = (string) => `${LIGHT_CYAN}${string}${DEF_FOREGROUND}`;

export const lightWhite = (string) =>
  `${LIGHT_WHITE}${string}${DEF_FOREGROUND}`;

export const bgLightBlack = (string) =>
  `${BACKGROUND_LIGHT_BLACK}${string}${DEF_BACKGROUND}`;

export const bgLightRed = (string) =>
  `${BACKGROUND_LIGHT_RED}${string}${DEF_BACKGROUND}`;

export const bgLightGreen = (string) =>
  `${BACKGROUND_GREEN}${string}${DEF_BACKGROUND}`;

export const bgLightYellow = (string) =>
  `${BACKGROUND_YELLOW}${string}${DEF_BACKGROUND}`;

export const bgLightBlue = (string) =>
  `${BACKGROUND_BLUE}${string}${DEF_BACKGROUND}`;

export const bgLightMagenta = (string) =>
  `${BACKGROUND_MAGENTA}${string}${DEF_BACKGROUND}`;

export const bgLightCyan = (string) =>
  `${BACKGROUND_CYAN}${string}${DEF_BACKGROUND}`;

export const bgLightWhite = (string) =>
  `${BACKGROUND_WHITE}${string}${DEF_BACKGROUND}`;

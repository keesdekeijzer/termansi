class Termansi:
    FG_RED = "\033[31m"
    FG_GREEN = "\033[32m"
    FG_BLUE = "\033[34m"
    FG_BLACK = "\033[30m"
    FG_WHITE = "\033[37m"
    FG_YELLOW = "\033[33m"
    FG_CYAN = "\033[36m"
    FG_MAGENTA = "\033[35m"

    BG_RED = "\033[41m"
    BG_GREEN = "\033[42m"
    BG_BLUE = "\033[44m"
    BG_BLACK = "\033[40m"
    BG_WHITE = "\033[47m"
    BG_YELLOW = "\033[43m"
    BG_CYAN = "\033[46m"
    BG_MAGENTA = "\033[45m"

    COLOR_RESET = "\033[0m"

    SAVE_CURSOR = "\033[s"
    RESTORE_CURSOR = "\033[u"

    MOVE_CURSOR_UP = "\033[A"
    MOVE_CURSOR_DOWN = "\033[B"
    MOVE_CURSOR_LEFT = "\033[C"
    MOVE_CURSOR_RIGHT = "\033[D"

    HIDE_CURSOR = "\033[?25l"
    SHOW_CURSOR = "\033[?25h"

    SET_BOLD = "\033[1m"
    SET_UNDERLINE = "\033[4m"
    SET_INVERSE = "\033[7m"
    SET_BLINK = "\033[5m"
    SET_HIDDEN = "\033[8m"
    SET_STRIKETHROUGH = "\033[9m"
    SET_RESET = "\033[0m"
    SET_RESET_BOLD = "\033[21m"
    SET_RESET_UNDERLINE = "\033[24m"
    SET_RESET_INVERSE = "\033[27m"
    SET_RESET_BLINK = "\033[25m"
    SET_RESET_HIDDEN = "\033[28m"
    SET_RESET_STRIKETHROUGH = "\033[29m"
    SET_RESET_ALL = "\033[0m"
    SET_RESET_ALL_BOLD = "\033[21m"
    SET_RESET_ALL_UNDERLINE = "\033[24m"
    SET_RESET_ALL_INVERSE = "\033[27m"
    SET_RESET_ALL_BLINK = "\033[25m"
    SET_RESET_ALL_HIDDEN = "\033[28m"
    SET_RESET_ALL_STRIKETHROUGH = "\033[29m"
    SET_RESET_ALL_COLORS = "\033[39m"
    SET_RESET_ALL_BACKGROUND_COLORS = "\033[49m"
    SET_RESET_ALL_FOREGROUND_COLORS = "\033[39m"
    SET_RESET_ALL_FOREGROUND_COLORS_AND_BACKGROUND_COLORS = "\033[39m\033[49m"
    SET_RESET_ALL_FOREGROUND_COLORS_AND_BACKGROUND_COLORS_AND_ATTRIBUTES = "\033[39m\033[49m\033[0m"
    SET_RESET_ALL_FOREGROUND_COLORS_AND_BACKGROUND_COLORS_AND_ATTRIBUTES_AND_CURSOR_POSITION = "\033[39m\033[49m\033[0m\033[s"
    SET_ITALIC = "\033[3m"
    SET_RESET_ITALIC = "\033[23m"

def main():
    print("Hello from termansi!")
    hello = f"{Termansi.FG_RED}Hello{Termansi.COLOR_RESET}"
    print(hello)
    test_print_colors()


    

def test_print_colors():
    print(f"{Termansi.FG_RED}This is red text{Termansi.COLOR_RESET}")
    print(f"{Termansi.FG_GREEN}This is green text{Termansi.COLOR_RESET}")
    print(f"{Termansi.FG_BLUE}This is blue text{Termansi.COLOR_RESET}")
    print(f"{Termansi.FG_BLACK}This is black text{Termansi.COLOR_RESET}")
    print(f"{Termansi.FG_WHITE}This is white text{Termansi.COLOR_RESET}")
    print(f"{Termansi.FG_YELLOW}This is yellow text{Termansi.COLOR_RESET}")
    print(f"{Termansi.FG_CYAN}This is cyan text{Termansi.COLOR_RESET}")
    print(f"{Termansi.FG_MAGENTA}This is magenta text{Termansi.COLOR_RESET}")
    print(f"{Termansi.SET_BOLD}This is bold text{Termansi.COLOR_RESET}")
    print(f"{Termansi.SET_UNDERLINE}This is underlined text{Termansi.COLOR_RESET}")
    print(f"{Termansi.SET_INVERSE}This is inverse text{Termansi.COLOR_RESET}")
    print(f"{Termansi.SET_BLINK}This is blinking text{Termansi.COLOR_RESET}")
    print(f"{Termansi.SET_HIDDEN}This is hidden text{Termansi.COLOR_RESET}")
    print(f"{Termansi.SET_STRIKETHROUGH}This is struckthrough text{Termansi.COLOR_RESET}")
    print(f"{Termansi.SET_ITALIC}This is italic text{Termansi.COLOR_RESET}")


if __name__ == "__main__":
    main()

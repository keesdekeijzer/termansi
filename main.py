def main():
    print("Hello from termansi!")


    FG_RED = "\033[31m"
    FG_GREEN = "\033[32m"
    FG_BLUE = "\033[34m"

    COLOR_RESET = "\033[0m"

    print(f"{FG_RED}This is red text{COLOR_RESET}")
    print(f"{FG_GREEN}This is green text{COLOR_RESET}")
    print(f"{FG_BLUE}This is blue text{COLOR_RESET}")


if __name__ == "__main__":
    main()

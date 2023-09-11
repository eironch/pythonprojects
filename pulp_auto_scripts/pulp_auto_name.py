import pyautogui


def main():
    name = input("Input Tile Name: ")
    max_range = int(input("Input Width: ")) * int(input("Input Height: "))

    if max_range == "":
        max_range = 30
    else:
        max_range = int(max_range)

    for i in range(0, max_range):
        pyautogui.click(1320, 210)
        pyautogui.hotkey("ctrlleft", "a")
        pyautogui.typewrite(f"{name}{i}")
        pyautogui.typewrite(["enter", "right"])

    print("\nDone!")


if __name__ == "__main__":
    main()

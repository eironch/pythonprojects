import pyautogui

def main():
    name = input("Input Tile Name: ")
    maxRange = int(input("Input Width: ")) * int(input("Input Height: "))

    if maxRange == "":
        maxRange = 30
    else:
        maxRange = int(maxRange)

    for i in range(0,maxRange):
        pyautogui.click(1320, 210)
        pyautogui.hotkey("ctrlleft", "a")
        pyautogui.typewrite(f"{name}{i}")
        pyautogui.typewrite(["enter","right"])

    print("\nDone!")

if __name__ == "__main__":
    main()
import pyautogui

def main():
    name = input("Input Tile Name: ")
    maxRange = input("Input Max Range: ")

    if maxRange == "":
        maxRange == 30
    else:
        maxRange = int(maxRange)

    for i in range(1,maxRange + 1):
        pyautogui.click(1320, 210)
        pyautogui.hotkey("ctrlleft", "a")
        pyautogui.typewrite(f"{name}{i}")
        pyautogui.typewrite(["enter","right"])

if __name__ == "__main__":
    main()
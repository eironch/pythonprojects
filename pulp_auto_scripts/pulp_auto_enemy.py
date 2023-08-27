import pyautogui

def main():
    direction = ["N", "E", "S", "W"]
    index = 0
    name = input("Input Tile Name: ")
    enemyCount = int(input("Input Enemy Count: "))
    enemyHealth = 1

    for i in range(enemyCount * 4):
        pyautogui.click(1320, 210)
        pyautogui.hotkey("ctrlleft", "a")
        pyautogui.typewrite(f"{name}{enemyHealth}{direction[index]}")
        pyautogui.typewrite(["enter", "right"])
        with pyautogui.hold('shift'):
            pyautogui.click(1135, 245)
        pyautogui.typewrite(["right"])

        if index == len(direction) - 1:
            index = 0
            enemyHealth += 1

            with pyautogui.hold('shift'):
                pyautogui.click(1280, 640)
            for x in range(3):
                with pyautogui.hold('shift'):
                    pyautogui.click(1290, 600)
            pyautogui.typewrite(["right"])
            with pyautogui.hold('shift'):
                pyautogui.click(1135, 245)
            pyautogui.typewrite(["right"])

        else:
            index += 1

    print("\nDone!")


if __name__ == "__main__":
    main()
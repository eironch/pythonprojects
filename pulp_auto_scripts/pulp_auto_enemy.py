import pyautogui

def check_pos():
    while True:
        print(pyautogui.position())

def main():
    direction = ["N", "E", "S", "W"]
    index = 0
    enemy_name = input("Input Tile Name: ")
    enemy_count = int(input("Input Enemy Count: "))
    enemy_health = 1

    for i in range(enemy_count * 4):
        pyautogui.click(1320, 210)
        pyautogui.hotkey("ctrlleft", "a")
        pyautogui.typewrite(f"{enemy_name}{enemy_health}{direction[index]}")

        pyautogui.click(1180, 770)
        pyautogui.click(1200, 830)
        pyautogui.typewrite("on any do")
        pyautogui.typewrite(["enter"])
        pyautogui.typewrite(f"mimic \"{enemy_name}Script\"")
        pyautogui.click(1200, 700)

        pyautogui.typewrite(["right"])

        with pyautogui.hold('shift'):
            pyautogui.click(1135, 245)
        pyautogui.typewrite(["right"])

        if index == len(direction) - 1:
            index = 0
            enemy_health += 1

        else:
            index += 1

    print("\nDone!")


if __name__ == "__main__":
    main()
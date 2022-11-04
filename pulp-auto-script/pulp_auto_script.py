import sys

def main():
    run_program = input("Which method to run? ")
    if run_program == "1":
        tile_operation()
    elif run_program == "2":
        update_tiles()
    elif run_program == "3":
        replace_word()
    elif run_program == "4":
        swap_building()
    elif run_program == "5":
        draw_building()
    elif run_program == "6":
        draw_transition()
    elif run_program == "7":
        update_tiles_off_screen()


def tile_operation():  # 1
    for x in range(25):
        for y in range(15):
            print(f'\non doTilex{x}y{y} do')
            for room in range(5):
                if room == 0:
                    print(f'  if checkRoom == "room{room}" then')
                else:
                    print(f'  elseif checkRoom == "room{room}" then')
                print(f'    if tileOperation == "save" then')
                print(f'      tilex{x}y{y}room{room} = tileNameSave')
                print(f'    elseif tileOperation == "swap" then')
                print(f'      if tileNameSwap != tilex{x}y{y}room{room} then')
                print(f'        tell {x},{y} to')
                print(f'          swap tilex{x}y{y}room{room}')
                print(f'        end')
                print(f'      end')
                print(f'    elseif tileOperation == "check" then')
                print(f'      tileNameCheck = tilex{x}y{y}room{room}')
                print(f'    elseif tileOperation == "change" then')
                print(f'      tilex{x}y{y}room{room} = tileNameChange')
                print(f'    end')

            print(f'  end')
            print(f'end')


def update_tiles_off_screen():  # 7
    start_x = 3
    y = 13
    print(f'on swapNutriDispenserOffScreen do')
    print(f'  tileOperation = "change"')
    print('')
    print(f'  tell "main.tile" to')
    for amount in range(0, 31):
        if amount in [4, 12, 20, 28]:
            y -= 1
            start_x += 5

        if amount == 0:
            print(f'    if amount == {amount} then')
        else:
            print(f'    elseif amount == {amount} then')

        print(f'      tileNameChange = "nutridispenser{amount}x{start_x}"')
        print( '      call "doTilex{x}' + f'y{y}"')

        if amount in [3, 11, 19, 27]:
            print(f'      tileNameChange = "nutridispenser0x{start_x + 5}"')
            print('      call "doTilex{x}' + f'y{y - 1}"')

    print(f'    end')
    print(f'  end')
    print(f'end')


# water tank
"""
def update_tiles_off_screen():  # 7
    start_x = 4
    y = 12
    print(f'on swapWaterTankOffScreen do')
    print(f'  swapX = x')
    print(f'  tileOperation = "change"')
    print(f'')
    print(f'  tell "main.tile" to')
    for amount in range(0, 23):
        if amount in [2, 10, 18]:
            y -= 1
            start_x += 4

        if amount == 0:
            print(f'    if amount == {amount} then')
        else:
            print(f'    elseif amount == {amount} then')

        count = 0
        x = start_x

        while count != 4:
            print(f'      tileNameChange = "watertank{amount}x{x}"')
            print( '      call "doTilex{swapX}' + f'y{y}"')

            if amount in [1, 9, 17]:
                print(f'      tileNameChange = "watertank0x{x + 4}"')
                print( '      call "doTilex{swapX}' + f'y{y - 1}"')

            count += 1
            x += 1
            if count != 4:
                print("      swapX++")

    print(f'    end')
    print(f'  end')
    print(f'end')
"""


def update_tiles():  # 2
    start_x = 8
    y = 11
    for amount in range(2, 23):
        if amount == 10 or amount == 18:
            y -= 1
            start_x += 4

        print(f'  elseif amount == {amount} then')
        count = 0
        x = start_x
        while count != 4:
            print(f'    tell swapX,{y} to'
                  f'      swap "watertank{amount}x{x}"'
                  f'    end')

            if amount == 9 or amount == 17:
                print(f'    tell swapX,{y - 1} to'
                      f'      swap "watertank0x{x}"'
                      f'    end')

            count += 1
            x += 1
            if count != 4:
                print("    swapX++")
    print("  end\n")


def replace_word():  # 3
    word_to_be_replaced = input("Input word to be replaced: ")
    word_to_replace = input("Input word to replace: ")
    print("Paste code, then CTRL + D to input.")
    code = sys.stdin.readlines()
    print("\nResult:\n")
    print(''.join(code).replace(word_to_be_replaced, word_to_replace))


def swap_building():  # 4
    building = "WaterTank"
    building_extension = "0x"
    building_dimension = 19
    building_width = 4

    print(f"on place{building} do")
    print(f'''  x = builderX
  y = builderY

  openSpace = 0
  repeat = 1

  call "checkSpace"

  if openSpace!=1 then
    done
  end

  currentEnergy += 2

  if currentEnergy>maxEnergy then
    currentEnergy -= 2
	done
  end\n''')

    for num in range(building_dimension + 1):
        if num % building_width == 0 and num != 0:
            print("""\n  x = builderX
  y--\n""")
        else:
            if num == 0:
                print('  x = builderX\n')
            else:
                print('  x++')

        print(f'''  tell x,y to
    swap "{building.lower()}{building_extension}{num}"
  end''')

    print('end')


def draw_building():  # 5
    building = "WaterTank"
    building_extension = "0x"
    building_dimension = 19
    building_width = 4
    builder_y = 13

    print(f'on draw{building} do')
    print(f'''  drawBuilderX = decimalBuilderX
  builderY = {builder_y}\n''')

    for num in range(building_dimension + 1):
        if num % building_width == 0 and num != 0:
            print('''\n  drawBuilderX = decimalBuilderX
  builderY--\n''')
        else:
            if num != 0:
                print('  drawBuilderX++')

        print(f'  draw "{building.lower()}{building_extension}{num}" at drawBuilderX,builderY')

    print(f'''\n  builderY = {builder_y}
end''')


def draw_transition():  # 6
    for num in range(0, 10):
        print(f'  if transitionFrame == {num} then')
        for x in range(25):
            for y in range(15):
                if num == 0:
                    print(f'    draw "black" at {x},{y}')
                else:
                    print(f'    draw "transition{num}" at {x},{y}')
        print(f'  end')


if __name__ == '__main__':
    main()

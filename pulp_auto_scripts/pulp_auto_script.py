import sys


def main():
    run_program = input("Which method to run? ")
    if run_program == "1":
        tile_operation()
    elif run_program == "2":
        update_tiles()
    elif run_program == "4":
        builder_place_building()
    elif run_program == "5":
        draw_building()
    elif run_program == "6":
        draw_transition()
    elif run_program == "7":
        update_tiles_off_screen()
    elif run_program == "8":
        builder_place_building_off_screen()
    elif run_program == "9":
        tell_tile()
    elif run_program == "10":
        swap_tile()
    elif run_program == "11":
        draw_tile()


def tile_operation():  # 1
    for x in range(25):
        for y in range(15):
            print(f'\non tilex{x}y{y} do')
            for room in range(5):
                if room == 0:
                    print(f'  if checkRoom == {room} then')
                else:
                    print(f'  elseif checkRoom == {room} then')
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
                print(f'    end')

            print(f'  end')
            print(f'end')


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

def builder_place_building():  # 4
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


def update_tiles_off_screen():  # 7
    start_x = 3
    y = 13
    building_sprite_length = 31

    print(f'  tileOperation = "change"')
    print('')
    print(f'  tell "main.tile" to')

    for amount in range(building_sprite_length):
        if amount in [4, 12, 20, 28]:
            y -= 1
            start_x += 5

        if amount == 0:
            print(f'    if amount == {amount} then')
        else:
            print(f'    elseif amount == {amount} then')

        print(f'      tileNameChange = "nutridispenser{amount}x{start_x}"')
        print('      call "doTilex{x}' + f'y{y}"')

        if amount in [3, 11, 19, 27]:
            print(f'      tileNameChange = "nutridispenser0x{start_x + 5}"')
            print('      call "doTilex{x}' + f'y{y - 1}"')

    print(f'    end')
    print(f'  end')
    print(f'end')


def builder_place_building_off_screen():  # 8
    building = "SolarPanel"
    building_extension = ""
    building_dimension = 15
    building_width = 8

    print(f'on swap{building}OffScreen do')
    print(f'  x = builderX')
    print(f'  y = builderY\n')

    print(f'  tell "main.tile" to')

    for num in range(building_dimension + 1):
        if num % building_width == 0 and num != 0:  # checks if the num is by {4}
            print(f'\n    x = builderX')
            print(f'    y--\n')
        else:
            if num !=0:
                print(f'    x++')

        print(f'    tileNameSave = "{building.lower()}{building_extension}{num}"')
        print('    call "doTilex{x}y{y}"')

    print(f'  end')
    print(f'end')

def tell_tile():  #9
    for x in range(25):
        for y in range(15):
            print(f'tell {x},{y} to')
            print(f'  call function')
            print(f'end')

def swap_tile():  #10
    structure = input("Structure name: ")
    structure_width = int(input("Structure width: "))
    structure_length = int(input("Structure length: "))
    structure_count = structure_width * structure_length
    print(f'')
    print(f'Result:')
    print(f'')

    print(f'on build_{structure} do')
    for x in range(structure_count):
        if x != 0:
            if x % structure_width == 0:
                print(f'  x -= {structure_width - 1}')
                print(f'  y++')
            else:
                print(f'  x++')
        else:
            print(f'  x = cursor_x')
            print(f'  y = cursor_y')
            print(f'  x -= 1')
            print(f'  y -= 1')
            print(f'')

        print(f'  tell x,y to')
        print(f'    swap "{structure}_{x}"')
        print(f'  end')
    print(f'end')

def draw_tile():  #11
    structure = input("Structure name: ")
    structure_width = int(input("Structure width: "))
    structure_length = int(input("Structure length: "))
    structure_count = structure_width * structure_length
    print(f'')
    print(f'Result:')
    print(f'')

    print(f'on draw_{structure} do')
    for x in range(structure_count):
        if x != 0:
            if x % (structure_width) == 0:
                print(f'  x -= {structure_width - 1}')
                print(f'  y++')
            else:
                print(f'  x++')
        else:
            print(f'  x = cursor_x')
            print(f'  y = cursor_y')
            print(f'  x -= 1')
            print(f'  y -= 1')
            print(f'')

        print(f'  draw "{structure}_{x}" at x,y')
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



if __name__ == '__main__':
    main()


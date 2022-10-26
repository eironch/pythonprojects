def main():
    run_program = input("Which method to run? ")
    if run_program == "1":
        save_tiles()
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


def save_tiles():  # 1
    for x in range(20, 25):
        for y in range(15):
            print(f'on zsaveTilex{x}y{y} do')
            for room in range(80):
                if room == 0:
                    print(f' if event.room == "room{room}" then')
                else:
                    print(f' elseif event.room == "room{room}" then')
                print(f'   tilex{x}y{y}room{room} = tileNameCheck')

                if room == 79:
                    print(f' end')

            print("end\n")


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
            print(f'    tell swapX,{y} to\n      swap "watertank{amount}x{x}"\n    end')
            if amount == 9 or amount == 17:
                print(f'    tell swapX,{y - 1} to\n      swap "watertank0x{x}"\n    end')
            count += 1
            x += 1
            if count != 4:
                print("    swapX++")
    print("  end\n")


def replace_word():  # 3
    code = ''''''
    print(code.replace("drawBuilderX", "previewBuilderX"))


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

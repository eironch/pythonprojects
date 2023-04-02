def main():
    def draw_code(name, width, height, variable_name):
        name = input("Input Sprite Name: ")
        width = int(input("Input Width: "))
        height = int(input("Input Height: "))
        variable_name = input("Input Variable Name: ")
        startingHeight = 7 - height
        frameCount = 0

        print("\nResult: \n")

        print(f'on draw{name} do')
        print(f'  {variable_name}DrawX = {variable_name}DecimalX\n')

        for x in range(width):
            # start it with the first frame count
            frameCount = x - width

            for i in range(1, height + 1):
                # changes frame count to accomodate y axis
                frameCount = frameCount + width

                print(f'  draw "{name[0].lower()}{name[1:]}{frameCount}" at {variable_name}DrawX,{startingHeight + i}')
            if x != width - 1:
                print(f'  {variable_name}DrawX++')

        print('end')

    def swap_code():
        name = input("Input Sprite Name: ")
        width = int(input("Input Width: "))
        height = int(input("Input Height: "))
        startingHeight = 7 - height
        frameCount = 0

        print("\nResult: \n")

        print(f'on swap{name} do')
        print(f'  x = builderX')
        print(f'  y = {startingHeight}\n')

        for frameCount in range(height*width):
            print(f'  tell x,y to')
            print(f'    swap "{name[0].lower()}{name[1:]}{frameCount}"')
            print(f'  end')

            if frameCount!=(height*width) - 1:
                if frameCount != 0:
                    if (frameCount + 1) % width != 0:
                        print(f'  x++')
                    else:
                        print(f'\n  x = builderX')
                        print(f'  y++\n')
                else:
                    print(f'  x++')

        print('end')

    build_code = input("Input Code to Build: ")

    if build_code == "1":
        draw_code()
    elif build_code == "2":
        swap_code()






if __name__ == "__main__":
    main()
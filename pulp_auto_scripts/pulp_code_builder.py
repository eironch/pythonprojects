def main():
    name = input("Input Sprite Name: ")
    width = int(input("Input Width: "))
    height = int(input("Input Height: "))
    variable_name = input("Input Variable Name: ")
    if variable_name == "player":
        startingHeight = 7 - height
    else:
        startingHeight = 6 - height

    frameCount = 0

    print("\nResult: \n")

    print(f'on draw{name} do')
    print(f'  {variable_name}DrawX = {variable_name}DecimalX\n')
    for x in range(0, width):
        # start it with the first frame count
        frameCount = x - width

        for i in range(1, height + 1):
            # changes frame count to accomodate y axis
            frameCount = frameCount + width

            print(f'  draw "{name[0].lower()}{name[1:]}{frameCount}" at {variable_name}DrawX,{startingHeight + i}')
        if x != width - 1:
          print(f'  {variable_name}DrawX++')
    print('end')

if __name__ == "__main__":
    main()
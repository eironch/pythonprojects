def main():
    tile_name = input("Input Name: ")
    var_name = input("Input Var Name: ")
    width = int(input("Input Width: "))
    height = int(input("Input Height: "))
    index = 0

    print("\nResult:\n")
    for y in range(height):
        for x in range(width):
            if x != 0:
                print(f"{var_name}X++")
            print(f'draw "' + tile_name + f'{index}" at posX,posY')
            index += 1

        if (y != height-1):
            print(f'{var_name}X-={width-1}')
            print(f'{var_name}Y++')


if __name__ == "__main__":
    main()
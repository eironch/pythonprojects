import sys


def main():
    min_x = 0
    min_y = 0
    max_x = 0
    max_y = 0

    maker_type = int(input("Input Room Maker Type: "))
    maker_pos = int(input("Input Room Maker Position Kind: "))

    if maker_type == 0:
        if maker_pos == 1:
            min_x = 6
            min_y = 1
            max_x = 12
            max_y = 7
        elif maker_pos == 2:
            min_x = 12
            min_y = 1
            max_x = 18
            max_y = 7
        elif maker_pos == 3:
            min_x = 6
            min_y = 7
            max_x = 12
            max_y = 13
        elif maker_pos == 4:
            min_x = 12
            min_y = 7
            max_x = 18
            max_y = 13

    elif maker_type == 1:
        if maker_pos == 1:
            min_x = 6
            min_y = 1
            max_x = 18
            max_y = 7
        elif maker_pos == 2:
            min_x = 6
            min_y = 7
            max_x = 18
            max_y = 13

    elif maker_type == 2:
        if maker_pos == 1:
            min_x = 6
            min_y = 1
            max_x = 12
            max_y = 13
        elif maker_pos == 2:
            min_x = 12
            min_y = 1
            max_x = 18
            max_y = 13

    elif maker_type == 11:
        min_x = int(input("Input Starting X Position: "))
        min_y = int(input("Input Starting Y Position: "))
        max_x = int(input("Input Max X Position: "))
        max_y = int(input("Input Max Y Position: "))

    print("Paste the Tile Names, then CTRL + D to end Input.")
    tile_name_list = "\n" + ''.join(sys.stdin.readlines())
    i = 0
    tile = ""
    tile_list = []

    while i < len(tile_name_list):
        check_start = ""

        if i + 3 < len(tile_name_list):
            check_start = tile_name_list[i: i + 2] + tile_name_list[i + 1] + tile_name_list[i + 2]

        if check_start == "run":
            if tile != '':
                tile_list.append(tile)

            tile = ""
            i += 49

        if not tile_name_list[i].isspace():
            tile += tile_name_list[i]

        i += 1

    tile_list.append(tile)
    construct_script(tile_list, min_x, min_y, max_x, max_y)


def construct_script(tile_list, min_x, min_y, max_x, max_y):
    pos_x = min_x
    pos_y = min_y
    i = 0

    while pos_y <= max_y:
        while pos_x <= max_x:
            if i >= len(tile_list):
                break

            if tile_list[i] == "ground" or tile_list[i] == "black":
                i += 1

                pos_x += 1

                continue

            # print(f'checkTileName = name {pos_x},{pos_y}')
            # print(f'if checkTileName != "{tile_list[i]}" then')
            print(f'tell {pos_x},{pos_y} to')
            print(f'    swap "{tile_list[i]}"')
            print(f'end')
            # print(f'end')

            i += 1
            pos_x += 1

        pos_x = min_x
        pos_y += 1


if __name__ == "__main__":
    main()

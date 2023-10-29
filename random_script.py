import random


def main():
    result = ""

    for y in range(13):
        for x in range(13):
            print(f' on handleScreenX{x}Y{y} do')
            print(f' checkTile = BLANK')
            print(f' if action=="x++" then')

            print(f' screenX{x}Y{y}TileX++')

            print(f' elseif action=="x--" then')

            print(f' screenX{x}Y{y}TileX--')

            print(f' elseif action=="y++" then')

            print(f' screenX{x}Y{y}TileY++')

            print(f' elseif action=="y--" then')

            print(f' screenX{x}Y{y}TileY--')

            print(f' elseif action=="update" then')

            print(f' // args')

            print(f' action = "get"')

            print(f' tell "tileHandler" to')

            print(f' call "handleTileX' + "{" + f'screenX{x}Y{y}TileX' + "}" + "Y{" + f'screenX{x}Y{y}TileY' + "}\"")

            print(f' end')

            print(f' screenX{x}Y{y} = checkTile')

            print(f' end')

            print(f' end')



if __name__ == "__main__":
    main()
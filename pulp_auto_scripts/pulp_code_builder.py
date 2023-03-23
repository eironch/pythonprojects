def main():
    name = input("Input Building Name: ")
    height = int(input("Input Building height: "))
    width = int(input("Input Building Width: "))
    startingHeight = 7 - height
    buildingCount = 0
    print("\nResult: \n")
    for x in range(1, width + 1):
        buildingCount = x - width

        for i in range(1, height + 1):
            buildingCount = buildingCount + width
            print(f'draw "{name}{buildingCount}" at builderDrawX,{startingHeight + i}')
        if x != width:
          print("builderDrawX++")


if __name__ == "__main__":
    main()
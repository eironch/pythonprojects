import sys


def main():
    code_quantity = int(input("Input Quantity of Code to be Duplicated: "))

    print("Paste Code, then CTRL + D to end Input.")
    code = "\n" + ''.join(sys.stdin.readlines())
    print("\nResult:\n")

    for i in range(code_quantity + 1):
        print(code.replace(str(1), str(i)))


if __name__ == "__main__":
    main()

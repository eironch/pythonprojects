import sys


def main():
    code_quantity = int(input("Input Quantity of Code to be Duplicated: "))
    num_to_be_replaced = input("Input Starting Number: ")
    print("Paste Code, then CTRL + D to end Input.")
    code = "\n" + ''.join(sys.stdin.readlines())
    print("\nResult:\n")

    for i in range(1, code_quantity + 1):
        print(code.replace(num_to_be_replaced, str(i)))


if __name__ == "__main__":
    main()

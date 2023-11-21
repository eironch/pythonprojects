import sys
import pyperclip


def main():
    result = ""
    code_quantity = int(input("Input Quantity of Code to be Duplicated: "))
    num_to_be_replaced = input("Input Starting Number: ")
    print("Paste Code, then CTRL + D to end Input.")
    code = "\n" + ''.join(sys.stdin.readlines())
    print("\nResult:")

    for i in range(1, code_quantity + 1):
        result += code.replace(num_to_be_replaced, str(i))

    print(result)
    print("\nCopied to Clipboard!")
    pyperclip.copy(result)

if __name__ == "__main__":
    main()

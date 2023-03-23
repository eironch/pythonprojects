import sys

def main():
    word_to_be_replaced = input("Input word to be replaced: ")
    word_to_replace = input("Input word to replace: ")
    print("Paste code, then CTRL + D to input.")
    code = "\n" + ''.join(sys.stdin.readlines())
    print("\nResult:\n")
    print(code.replace(word_to_be_replaced, word_to_replace))


if __name__ == "__main__":
    main()
import sys

def main():
    word_to_be_replaced = input("Input Word to be Replaced: ")
    word_to_replace = input("Input Word to Replace: ")
    print("Paste Code, then CTRL + D to end Input.")
    code = "\n" + ''.join(sys.stdin.readlines())
    print("\nResult:\n")
    print(code.replace(word_to_be_replaced, word_to_replace))


if __name__ == "__main__":
    main()
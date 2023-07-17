import sys


def main():
    word_to_be_replaced_list = []
    word_to_replace_list = []

    for i in range(int(input("Input number of words to replace: "))):
        word_to_be_replaced_list.append(input("Input word to be replaced: "))
        word_to_replace_list.append(input("Input word to replace: "))

    print("Paste Code, then CTRL + D to end Input.")
    code = "\n" + ''.join(sys.stdin.readlines())
    print("\nResult:\n")

    for i in range(len(word_to_be_replaced_list)):
        code = code.replace(word_to_be_replaced_list[i], word_to_replace_list[i])

    print(code)


if __name__ == "__main__":
    main()

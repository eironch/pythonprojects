import time
import string as alphabet_import


# checks if input has uppercase
def alphabet(string):
    alphabet_list = list(alphabet_import.ascii_lowercase)
    alphabet_list.append(" ")

    for letter in string:
        if letter.isupper():
            alphabet_list = list(alphabet_import.ascii_letters.append(" "))
            alphabet_list.append(" ")

    return alphabet_list


def output(string):
    sentence = []
    output_string = ""
    index = 0

    while True:
        for letter in alphabet(string):
            time.sleep(0.05)

            # inserts the indexed letter and joins it
            if output_string != string:
                sentence.insert(index, letter)
                output_string = "".join(sentence)

            print(output_string)

            if output_string != string:
                # checks if the current letter is not the same as the target letter
                if not letter == string[index]:
                    sentence.pop(index)
                else:
                    # checks if the current output is not the target word
                    if index != len(string) - 1:
                        index += 1
                        break


output(input("Type your desired word, phrase, or sentence... Press enter to commence.\n"))
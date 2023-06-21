import sys
import webbrowser


def main():
    print("Paste Urls, then CTRL + D to end Input.")
    urls = "\n" + ''.join(sys.stdin.readlines())
    index = 0

    while index <= len(urls):
        if (urls[index] == "u" and urls[index + 1] == "r"
                and urls[index + 2] == "i" and urls[index + 3] == "=" and index + 3 < len(urls)):
            index += 4
            letter_count = index
            while letter_count <= len(urls):
                if letter_count + 6 < len(urls):
                    if (urls[letter_count] == "c" and urls[letter_count + 1] == "h"
                            and urls[letter_count + 2] == "r" and urls[letter_count + 3] == "o"
                            and urls[letter_count + 4] == "m"):
                        break

                    letter_count += 1
            url = ""
            letter_index = index
            while letter_index <= letter_count - 3:
                url = url + urls[letter_index]

                letter_index += 1

            index = letter_count

            webbrowser.open(url)
        else:
            index += 1


if __name__ == "__main__":
    main()
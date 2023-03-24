import random

def main():
    name = "cheiron"
    output = []

    for x in range(len(name)):
        append_random_char("cheiron", output, random.randint(0, len(name) - 1))

    print("".join(output))

def append_random_char(name, output, rand_num):
    if name[rand_num] not in output:
        output.append(name[rand_num])

    else:
        append_random_char("cheiron", output, random.randint(0, len(name) - 1))

if __name__ == "__main__":
    main()
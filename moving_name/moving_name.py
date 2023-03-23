import time

def main():
    name = list("cheiron")
    while True:
        name.insert(0, name[len(name) - 1])
        name.pop()
        print("".join(name))
        time.sleep(0.01)

if __name__ == "__main__":
    main()
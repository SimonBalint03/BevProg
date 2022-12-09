def main():
    with open("Hazik/string_1.txt", "r") as f, open("Hazik/string1_clean.txt", "w") as g:
        txt = f.readlines()
        for i in txt:
            if i.find("#") == int(-1) and i != "\n":
                print(i, file=g, end="\n")
            elif i != '\n':
                index = i.rfind("#") + 1
                if i[index-len(i)].isspace() is False:
                    print(i[index-len(i)], file=g, end="")


if __name__ == "__main__":
    main()

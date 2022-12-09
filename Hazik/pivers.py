def main():
    with open("Hazik/pivers.txt", "r") as f:
        txt = f.read().split()
        szamok = []
        for i in txt:
            szamok.append(len(i))
        print(szamok[0])


if __name__ == "__main__":
    main()

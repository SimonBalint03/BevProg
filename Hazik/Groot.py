import random

def main():
    li = ["G","R","O","T"]
    li2 = []
    szamlalo = 0
    hurra = False
    while hurra is False:
        for i in range(5):
            rndLetter = random.choice(li)
            li2.append(rndLetter)
        if li2[0] == "G" and li2[1] == "R" and li2[2] == "O" and li2[3] == "O" and li2[4] == "T":
            print(li2)
            print("Hurrá, csak: {0} alkalomra találta el.".format(szamlalo))
            hurra = True
        else:
            szamlalo += 1
            li2 = []

if __name__ == "__main__":
    main()

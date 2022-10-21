def tukroz(stri):
    # Megnézzük a szám hosszát, majd a végétől fogva visszafele olvassuk.
    striLen = len(stri)
    slice = stri[striLen::-1]
    return slice


def isTukorSzam(sz):
    szamFele = round(len(str(sz))/2) # A szám középpontja.
    balOldal = str(sz)[:szamFele]
    jobbOldal = str(sz)[- szamFele:]
    if tukroz(balOldal) == jobbOldal:
        return "A(z) {0} tükörszám!".format(sz)
    else:
        return "A(z) {0} nem tükörszám!".format(sz)


def main():
    sz = int(input("Írd be a számot: "))
    print(isTukorSzam(sz))


if __name__ == '__main__':
    main()

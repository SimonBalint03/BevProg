from math import pi

def kor():
    r = int(input("A kör sugara = "))
    print("A kör területe: {0}cm²".format(round((r**2)*pi, 2)))
    
def teglalap():
    a = int(input("a = "))
    b = int(input("b = "))
    print("A téglalap területe: {0}cm²".format(round(a*b, 2)))
    
def kup():
    r = int(input("A alapon fekvő kör sugara (r) = "))
    m = int(input("Az alaptól számított magassága (m) = "))
    
    V = (((r**2) * pi) * m) / 3
    print("A kúp térfogata: {0}cm³".format(round(V,2)))

def main():
    print("1. Kör Területe | 2. Téglalap területe | 3. Kúp Térfogata")
    tetelId = int(input("Válassz a képletek közül: "))

    if tetelId == 1:
        kor()
    elif tetelId == 2:
        teglalap()
    elif tetelId == 3:
        kup()
    else:
        main()


if __name__ == "__main__":
    main()

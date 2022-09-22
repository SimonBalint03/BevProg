from asyncio.windows_events import NULL
import cmath
from contextlib import nullcontext
from math import sqrt


def pitagorasz():
    print("Pitagorasz-Tétel: ")
    a = int(input("a² = "))
    b = int(input("b² = "))

    jobbOldal = a**2 + b**2

    print("c² = {0}".format(sqrt(jobbOldal)))


def masodfoku():
    print("Másodfokú egyenlet: ")
    a = int(input("a = "))
    b = int(input("b = "))
    c = int(input("c = "))

    diszkriminans = (b**2) - (4*a*c)

    x1 = (-b-cmath.sqrt(diszkriminans))/(2*a)
    x2 = (-b+cmath.sqrt(diszkriminans))/(2*a)

    # x1-re
    print("x1= {0} | x2= {1} ".format(x1, x2))


def trapez():
    print("Trapéz felszíne: ")
    a = int(input("a = "))
    b = int(input("b = "))
    m = int(input("m: "))

    felszin = ((a + b) / 2) * m

    print("A trapéz felszíne: {0}".format(felszin))


def main():
    print("1. Pitagorasz-Tétel | 2. Másodfokú egyenlet | 3. Trapéz felszíne")
    tetelId = int(input("Válassz a képletek közül: "))

    if tetelId == 1:
        pitagorasz()
    elif tetelId == 2:
        masodfoku()
    elif tetelId == 3:
        trapez()
    else:
        main()


if __name__ == "__main__":
    main()

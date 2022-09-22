def main():
    eletKor = int(input("Írd be az életkorod: "))

# 1. feladat
    if eletKor >= 21:
        print("1. Fogyaszthatsz legálisan alkoholt Amerikában!")
    else:
        print("1. Nem fogyaszthatsz legálisan alkoholt Amerikában!")
# 2. feladat
    if eletKor >= 18:
        print("2. Vásárolhatsz dohányterméket Magyarországon!")
    else:
        print("2. Nem vásárolhatsz19 dohányterméket Magyarországon!")
# 3. feladat
    if eletKor >= 16:
        print("3. Szerezhetsz jogosítványt!")
    else:
        print("3. Nem szerezhetsz jogosítványt!")
# 4. feladat
    if eletKor >= 12:
        print("4. Megnézheted a Shrek 2-t egyedül! :)")
    else:
        print("4. Nem nézheted meg a Shrek 2-t egyedül!")
        
    

if __name__ == "__main__":
    main()

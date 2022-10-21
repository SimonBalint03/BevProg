def binaris(szam, li = []):
    if szam >= 1:
        if szam % 2 == 1:
            li.append(1)
            binaris(round(szam//2))
        else:
            li.append(0)
            binaris(round(szam//2))
    return (''.join(str(i) for i in li))

def main():
    szam = int(input("Írj be egy számot: "))
    print("{0} binárisan = {1}".format(szam, binaris(szam)))

main()

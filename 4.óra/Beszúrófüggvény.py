def beszur(keresettSzo, beszurtSzo, szoveg="Az egy bögre"):
    szovegList = szoveg.split(" ")
    i = 0
    for index in szovegList:
        i += 1
        if index == keresettSzo:
            szovegList.insert(i-1, beszurtSzo)
            return ' '.join(szovegList)

def main():
    print(beszur('bögre', 'piros'))


main()

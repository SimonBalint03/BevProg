def valid(text, chars="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"):
    matchList = []
    for i in text:  # Végig megyünk a text összes karakterén
        for j in chars:  # Végig megyünk a chars összes karakterén
            if i == j:  # Ha a jelenleg vizsgált két karakter megegyezik:
                matchList.append(j)

    return matchList


def main():
    print(valid("KL754", "0123456789"))


main()

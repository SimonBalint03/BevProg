def caesarDecode(stri):
    codeList = []
    for index in stri:
        o = ord(index)
        if index.isupper():
            if ord('A') < o+2 > ord('Z'):
                o = o-26
            codeList.append(o+2)
        elif index.islower():
            if ord('a') < o+2 > ord('z'):
                o = o-26
            codeList.append(o+2)
        else:
            codeList.append(o)

    i = 0

    for index in codeList:
        codeList[i] = chr(index)
        i += 1
    return ''.join(codeList)


def main():
    f = open("11.óra/fater.txt", "r")
    for i in f:
        print(caesarDecode(i), end="")
    f.close


if __name__ == "__main__":
    main()

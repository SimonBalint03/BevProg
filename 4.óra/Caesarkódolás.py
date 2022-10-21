def caesarDecode(stri):
    codeList = []
    for index in stri:
        codeList.append(ord(index)-3)
    
    i = 0
    for index in codeList:
        codeList[i] = chr(index)
        i += 1
    return ''.join(codeList)

def main():
    stri = "kwwsv=22|rxwx1eh2gTz7z<Zj[fT"
    print(caesarDecode(stri))
    
if __name__ == "__main__":
    main()
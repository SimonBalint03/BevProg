def main():
    c1 = """Totya is a hideous duck. His nose is enourmous , his wings look terribe and he
            doesn't have any feather on his head. Even that Totya is always immaculate since
            he spends most of his time in water. It doesn't matter if his bath is freezing or
            boiling he takes a shower every day!"""

    li = list(c1.split(" "))
    print(li)
    
    csunyaSzavak = {
        "hideous" : "very ugly",
        "enourmous" : "very big",
        "immaculate" : "perfect"
    }
    
    for word in li:
        if word in csunyaSzavak:
            print(csunyaSzavak[word], end= ' ')
        else:
            print(word, end=' ')
    

if __name__ == '__main__':
    main()
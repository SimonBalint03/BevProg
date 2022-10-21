def osszeg(lista):
    if len(lista) == 0:
        return 0
    elif len(lista) == 1:
        return lista[0]
    else:
        return lista[0] + osszeg(lista[1:]) # lista[1:] 1-től length elemig elszámol
    

def main():
    egeszek = [2,4,12,43,12,65]
    print(osszeg(egeszek))
    
if __name__ == "__main__":
    main()
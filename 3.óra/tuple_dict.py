def main():
    kartya = (1, "Bálint", 4.5)
    id, nev, jegy = kartya
    print(kartya)
    
    
    osztalyzat = {
        "Anna" : 4.5,
        "Béla" : 2,
        "Cecilia" : 1,
    }
    
    print(osztalyzat.keys())
    print(osztalyzat.values())
    print(osztalyzat.items())
    print(len(osztalyzat))

if __name__ == '__main__':
    main()
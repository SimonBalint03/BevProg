def main():
    
    beSzoveg = input("Mit szeretnél írni a fájlba?: ")
    with open("Hazik/Doboz.txt", "a") as f:
        print("Python: "+ beSzoveg,file=f)
        
        
if __name__ == "__main__":
    main()

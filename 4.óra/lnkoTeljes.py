def lnko(a,b):
    while not (a == b):   # while not (a == b)
        if (a > b):
            a -= b
        elif (a < b):
            b -= a
        return a

def main():
    print(lnko(10,3))
    
if __name__ == "__main__":
    main()
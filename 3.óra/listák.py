def main():

    xLista = {2, 6, 9, 12, 15, 18, 26, 543}
    yLista = {2, 9, 321, 43, 123, 2134, 12, 15}
    
    for index in xLista:
        if index in yLista:
            print(index, end = ",")


if __name__ == "__main__":
    main()

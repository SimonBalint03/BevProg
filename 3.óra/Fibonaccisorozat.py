def nTag(n):
    if n < 2:
        return n
        # Első elem esetén önmaga lesz a válasz.
    else:
        return nTag(n-1) + nTag(n-2)
        # Megnézzük a tag előtti két számot és összeadjuk.


def main():
    print(nTag(15))


if __name__ == '__main__':
    main()

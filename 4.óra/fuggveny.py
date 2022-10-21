def foo(a, b=5, c=4):
    a = a+b-c
    return (a, b)


def rec(a):
    print(a)
    if a < 1:
        return a
    return rec(a-1)
    return rec(a)


def main():
    foo(6, c=2)
    a = 2
    a = foo(a)
    print(a)
    print(rec(3))


if __name__ == "__main__":
    main()

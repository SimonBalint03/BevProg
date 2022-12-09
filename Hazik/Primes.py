def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    maxi = n**0.5 + 1
    while i <= maxi:
        if n % i == 0:
            return False
        i += 2

    return True


def main():
    # 100 alatti prímek
    li = []
    for i in range(99):
        if is_prime(i):
            li.append(i)
    print(','.join(str(i) for i in li))
    
    # 200 alattiak összege
    cntr = 0
    for i in range(200):
        if is_prime(i):
            cntr += i
    print(cntr)


if __name__ == "__main__":
    main()

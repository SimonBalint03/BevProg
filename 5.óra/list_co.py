def main():
    li = [n*2 for n in range(0,10)]
    print(li)
    
    li2 = ['auto','villamos','metro']
    li = [s.upper()+'!' for s in li2]
    
    li.clear()
    for s in li2:
        s = s.upper() + '!'
        li.append(s)
    print(li)

if __name__ == "__main__":
    main()
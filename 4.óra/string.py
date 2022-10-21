def both_ends(stri):
    if (len(stri) < 2):
        return " "
    return (stri[0:2]) + stri[-2:]  #A végéről kettővel vissza megy

def main():
    txt = "Hello World!"
    #   print(len(txt)) '13'
    #   print(txt[3]) 'l'
    #   print(txt[1:8]) 'ello Wo'
    #   print(txt.upper()) 'HELLO WORLD!'
    #   print(txt.capitalize()) 'Hello world!'
    #   print(txt.title()) 'Hello World!'
    #   print("           helo            ".strip()) 'helo'
    #   print(txt.replace("l","n")) 'Henno Wornd!'
    #   print("1;2;3;4;5".split(sep=';')) '['1', '2', '3', '4', '5']'
    print(both_ends("Katika"))
    
    
    
    
if __name__ == "__main__":
    main()
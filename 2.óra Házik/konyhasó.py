from sre_constants import JUMP


def main():

    na = int(input("Nátrium: "))
    cl = int(input("Klorid: "))

    nacl = 0
    excessNa = 0
    excessCl = 0
    
    if na == cl:
        nacl = na
    elif na > cl:
        if na % 2 == 0:
            nacl = na
        
            
    if na % 2 == 0:
        if cl % 2 == 0:
            


if __name__ == "__main__":
    main()

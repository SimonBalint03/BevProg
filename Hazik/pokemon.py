import requests

def main():
    isFail = False
    beNev = input("Melyik pokémont keresed?: ")
    try:
        j = requests.get("https://pokeapi.co/api/v2/pokemon/{0}".format(beNev))
        data = j.json()
    except:
        print("Nincs ilyen pokémon! :(")
        isFail = True
    if isFail is False:
        numAbilities = len(data["abilities"])
        pMove = data["moves"][0]["move"]["name"]  # primary move 

        health = data["stats"][0]["base_stat"] # élet
        attack = data["stats"][1]["base_stat"] # támadás
        defense = data["stats"][2]["base_stat"] # védelem
        speed = data["stats"][3]["base_stat"] # spíd
        print("{0} adatai: ".format(beNev))
        print(f"Health: {health}")
        print(f"Attack: {attack}")
        print(f"Defense: {defense}")
        print(f"Speed: {speed}")
        print(f"Primary Move: {pMove}")
        print(f"Number of abilities: {numAbilities}")


if __name__ == "__main__":
    main()

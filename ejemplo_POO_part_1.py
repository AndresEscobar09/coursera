class PartyAnimal:
    x=0
    def __init__(valor):
        print('I am constructed')

    def party(valor):
        valor.x =valor.x+1
        print("So far",valor.x)

    def __del__(valor):
        print('I am destructed', valor.x)

an = PartyAnimal()

an.party()
an.party()
#an.party()
an = 22
#print("Type", type(an))
#print("dir", dir(an))
print('an contains',an)

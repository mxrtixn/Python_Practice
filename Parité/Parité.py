def parité(number):

    if number % 2 ==0: print(number, " est pair")
    elif number % 2 !=0: print(number, " n'est pas pair")

number= int(input("Entrez le nombre entier: "))
parité(number)

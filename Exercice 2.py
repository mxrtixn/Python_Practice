def suite_fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return suite_fibonacci(n-1) + suite_fibonacci(n-2)
    
    
def main():
    n = int(input("Entrez le nombre de termes de la suite de Fibonacci (entre 0 et 30): "))

    for i in range(n):
            print(suite_fibonacci(i))


main()
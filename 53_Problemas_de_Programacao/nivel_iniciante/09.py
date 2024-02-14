def main():
    numeros = []
    while (1):
        numero = int(input(': '))
        if (numero !=0):
            numeros.append(numero)
            
        else:
            break
    print('sucessosres: ')
    for n in numeros:
        print (n + 1)

main()

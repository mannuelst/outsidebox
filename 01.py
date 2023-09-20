#Problema da soma
#Faça um programa capaz de solicitar um número N (1<N<1000) do usuário e ler N
#números inteiros. Após a leitura do último número deve-se informar:
#Na primeira linha a soma dos N números em decimal.
#Na segunda linha a soma em hexadecimal dos números pares informados.
#Na terceira linha a soma em octal dos números impares informados.
#Assuma que todos os números fornecidos pelo usuário serão inteiros válidos e que as
#somas nunca serão superiores a um número inteiro de 32 bits.

def prob_soma(tam):
    total=pares=impares=i=0
    while i<tam: 
        var_aux=int(input(": "))
        total+=var_aux
        if var_aux%2==0:
            pares+=var_aux
        else:
            impares+=var_aux
        i+=1
    
    print("A soma em decimal é: ", total)
    print("A soma em hexadecimal é: ", hex(pares))
    print("A soma em octal é: ", oct(impares))
        
def main():
    num= int(input("Digite um número: "))
    prob_soma(num)
    
main()
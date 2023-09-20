#4 Problema da sequência de Fibonacci
#A sequência de Fibonacci é construída de forma que cada termo é obtido pela soma dos
#dois termos anteriores. Por exemplo: 0, 1, 1, 2, 3, 5, 8, 13.
#Faça um programa capaz de solicitar um número inteiro N (1<=N<=40) e informar os N
#primeiros elementos (um elemento por linha) da sequência de Fibonacci a partir do zero e
#com o segundo elemento 1.
def fibonacci (num):
    if num<2:
        return 1
    else:
        return fibonacci(num-1)+fibonacci(num-2)
def prob_seq_fibb(n):
    for i in range(n):
        print (fibonacci(i))
   
def main():
    num=int(input("SEQUÊNCIA DE FIBONACCI\nValor de entrada: "))
    if num >0 and num<1000:
        print(prob_seq_fibb(num))
    else:
        print("Opsss...! O Número de estar no intervalo de 1 à 1000.")
        main()
    
    
main()
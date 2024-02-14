#2 Problema da média
#Faça um programa capaz de solicitar um número inteiro N (1<N<1000) do usuário e ler N
#números inteiros. Ao final da leitura do último número, o programa deverá informar, com
#uma casa decimal, a média aritmética entre os N números que estejam contidos no
#intervalo fechado entre -1000 e 1000.
#Assuma que todos os números fornecidos pelo usuário serão inteiros válidos e que a
#soma de todos os N nunca será superior a um número inteiro de 32 bits.
def prob_media(num):
    i_total=total=i_num=0
    while i_num<num:
        var_num=int(input(": "))
        if var_num>=-1000 and var_num<=1000:
            total+=var_num
            i_total+=1
        i_num+=1
    print("A media: ",float(total/i_total))

def main():
    num=int(input("Quantos números voce quer?\n: "))
    if num >0 and num<1000:
        prob_media(num)
    else:
        print("Opsss...! O Número de estar no intervalo de 1 à 1000.")
        main()

main()
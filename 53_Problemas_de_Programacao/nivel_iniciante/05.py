#5 Problema da conjectura de Goldbach
#A conjectura de Goldbach (ainda não provada) diz que qualquer número par maior ou
#igual a 4 é a soma de dois números primos.
#Faça um programa que, recebendo um número P par (2<=P<=4294967294), seja capaz
#de retornar dois número inteiros correspondentes aos dois números primos cuja soma
#seja igual ao número par P.
#Considere que:
#•
#•
#•
#Os valores de saída devem ser ordenados em ordem crescente.
#Existindo mais de uma combinação possível, retorna-se aquela cujo primeiro valor
#seja o menor.
#Não existindo valores (parabéns! você foi o primeiro no mundo que provou que a
#conjectura é falsa!) retorne -1.
#Lembre-se: número primo é todo número inteiro maior que 1 que somente é divisível por
#si próprio e pela unidade.
def is_primo(num):
    cont=0
    for i in range(1,num+1, 1):
        if (num%i==0):
            cont+=1
    if cont ==2: return True

def goldbach(num):
    back_num=front_num=0
    if num >=4:
        for i in range(num):
            if is_primo(i) and is_primo(num-i):
                back_num=i
                front_num=num-i
                if back_num + front_num == num:
                    print("",back_num," ",front_num)
                    break
                    
def main():
    num=int(input("A COJECTURA DE  GOLDBACH\nEntra com valor: "))
    if num >=2 and num<=4294967294:
        goldbach(num)
    else:
        print("Opsss...! O Número de estar no intervalo de 2 à 4294967294.")
        main()
main()            

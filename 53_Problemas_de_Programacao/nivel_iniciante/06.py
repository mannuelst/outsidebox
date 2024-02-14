#6 Problema do quadrado gêmeo das partes
#Existem alguns números que têm uma propriedade bastante interessante, observe:
#100
#10+0=10 10*10=100
#2025
#20+25=45 45*45=2025
#3025
#30+25=55 55*55=3025
#9801
#98+1=99 99*99=9801
#10000
#100+0=100 100*100=10000
#88209
#88+209=297 297*297=88209
#494209
#494+209=703 703*703=494209
#998001
#998+1=999 999*999=998001
#Os números que têm esta propriedade são conhecidos como número de Kaprekar.
#Cada um dos números apresentados tiveram seus algarismos decompostos de tal forma
#que a soma das partes elevado ao quadrado era igual ao número original.
#Faça um programa capaz de ler e identificar se um determinado número N
#(1<=N<=100.000.000) possui ou não esta propriedade. Caso positivo, o programa deverá
#retornar uma única linha com o valor 1, caso contrário deve-se retornar uma linha com
#valor 0.

def split_alg(num):
    str_num=str(num)
    list_alg=[]
    tam=len(num)
    for i in range(0, num+1, 2):
        list_alg.append(i)
    return list_alg
shift
print(split_alg(100))
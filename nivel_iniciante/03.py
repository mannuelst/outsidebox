#3 Problema do número espelho
#Faça um programa que recebendo um número inteiro positivo N em hexadecimal seja
#capaz de verificar se este número em decimal é lido exatamente da mesma forma seja de
#frente para trás ou de trás para frente.
#Caso positivo o programa deverá retornar uma linha com o caractere S, caso contrário o
#caractere informado deverá ser o N.
def prob_is_num_espelho(num):
    int_str = str(int(num, 16))
    if (int_str[::-1].lower()==int_str.lower()):
        return "S"
    return "N"
def main():
    num_hex=input("Entra com valor Hexadecimal: ")
    print(prob_is_num_espelho(num_hex))
    
main()
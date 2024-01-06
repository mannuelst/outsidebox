#include <stdio.h>
#include <stdlib.h>
// Leia dois valores inteiros A e B. Se A e B forem iguais, some-os; caso contrário, multiplique A por B. Imprima o resultado final.

int main()
{
    int num = 0;
    int num2 = 0;
    int result = 0;
    printf("Digite dois números");
    scanf("%d %d", &num, &num2);
    result = (num == num2) ? (num + num2) : (num * num2);
    printf("Resultado: %d ", result);
    system("pause");
    return 0;
}
#include <stdio.h>
#include <stdlib.h>

// Faça um algoritmo que leia os valores de A, B, C e imprima a soma de A e B. Em seguida, determine se essa soma é menor que C.
int main()
{
    int a = 0;
    int b = 0;
    int c = 0;

    printf("Digite o valor de a: ");
    scanf("%d", &a);
    printf("Digite o valor de b: ");
    scanf("%d", &b);
    printf("Digite o valor de c: ");
    scanf("%d", &c);

    printf("a+b= %d", (a + b));
    ((a + b) < c) ? printf("\n %d é maior que a soma %d e %d", c, a, b) : printf("\n A soma de %d e %d é maior que o valor de %d", a, b, c);

    system("pause");
    return 0;
}
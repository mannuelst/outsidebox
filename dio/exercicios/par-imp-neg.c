#include <stdio.h>

// Receba um número qualquer e imprima se é par ou ímpar, positivo ou negativo.

int main()
{
    float num;
    printf("Digite um número:");
    scanf("%f", &num);

    (num > 0) ? printf("\nNúmero Positivo") : printf("\nNúmero Negativo!");
    return 0;
}
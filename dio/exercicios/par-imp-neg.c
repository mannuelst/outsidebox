#include <stdio.h>

int main()
{
    float num;
    printf("Digite um número:");
    scanf("%f", &num);

    (num > 0) ? printf("\nNúmero Positivo") : printf("\nNúmero Negativo!");
    return 0;
}
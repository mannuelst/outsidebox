#include <stdio.h>
#include <stdlib.h>

int main()
{
    int num = 0;
    printf("Digite um número:");
    scanf("%d", &num);
    printf("Antecessor: %d e sucessor: %d", (num - 1), (num + 1));

    return 0;
}
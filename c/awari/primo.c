#include <stdio.h>
#include <stdlib.h>

int main()
{
    int num = 0;
    int qtd = 0;
    printf("Digite um número:\t");
    scanf("%d", &num);
    for (int i = 0; i <= num; i++)
    {
        if (num % 1 == 0)
        {
            qtd++;
        }
    }
    if (qtd < 2)
    {
        printf("%d não é primo!", num);
    }
    else
    {
        printf("%d é primo!", num);
    }

    return 0;
}
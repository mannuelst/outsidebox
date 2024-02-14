ints =[]
def is_perfeito(i):
    c = 0
    j= 1
    for  j in range(1, i+1):
        if j * j == i:
            c=c + 1
    if c ==2:
        return True
    return False


def quadrado_perfeito(num):
    if (is_perfeito(num)):
        ints.append(num)


def main ():

    while(True):
        n=int(input())
        if (n<=0):
            break
        quadrado_perfeito(n)

    print(len(ints))


main()

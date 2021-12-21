import math


def main():
    n = int(input())
    k = math.floor(math.log2(n))
    if n >= 2**(k+1):
        print(k+1)
    elif n < 2**k:
        print(k-1)
    else:
        print(k)


main()
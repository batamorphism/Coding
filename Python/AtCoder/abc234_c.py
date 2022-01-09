# 0,1からなる正整数のうち、K番目に大きいものは、
# 二進数のK
def main():
    k = int(input())
    bi = bin(k)[2:]
    bi = bi.replace('1', '2')
    ans = int(bi, 10)
    print(ans)


main()

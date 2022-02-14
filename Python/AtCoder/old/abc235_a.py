def main():
    A = list(input())
    A = list(map(int, A))
    val1 = A[2]*100+A[1]*10+A[0]
    val2 = A[1]*100+A[0]*10+A[2]
    val3 = A[0]*100+A[2]*10+A[1]
    ans = val1+val2+val3
    print(ans)


main()

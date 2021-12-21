def main():
    k = int(input())
    A, B = input().split()
    # k進数のaを10展開する
    a_10 = 0
    for a in A:
        a_10 = a_10*k
        a_10 += int(a)
    b_10 = 0
    for b in B:
        b_10 = b_10*k
        b_10 += int(b)
    print(a_10*b_10)


main()

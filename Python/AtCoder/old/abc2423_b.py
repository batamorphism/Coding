def main():
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    ans1 = 0
    for a, b in zip(A, B):
        if a == b:
            ans1 += 1

    ans2 = -ans1
    B_set = set(B)
    for a in A:
        if a in B_set:
            ans2 += 1

    print(ans1)
    print(ans2)


main()

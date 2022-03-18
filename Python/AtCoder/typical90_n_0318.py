def main():
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    ans = 0
    for a_i, b_i in zip(A, B):
        ans += abs(a_i-b_i)
    print(ans)


main()

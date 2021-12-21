# abs(A-B) == kか
def main():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    C = [abs(A[i]-B[i]) for i in range(n)]
    sum_c = sum(C)
    if sum_c <= k and (sum_c - k) % 2 == 0:
        print('Yes')
    else:
        print('No')


main()

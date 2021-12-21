def main():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    for _ in range(k):
        A = one_step(A)
        if sum(A) == n**2:
            break
    print(*A)


def one_step(A):
    B = [0] * len(A)
    n = len(A)
    # imos
    for i, a in enumerate(A):
        le = i-a
        ri = i+a+1
        le = max(0, le)
        B[le] += 1
        if ri < n:
            B[ri] -= 1
    for i in range(1, n):
        B[i] += B[i-1]
    return B


main()

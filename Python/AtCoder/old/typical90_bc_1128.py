# 100C5 = 75,287,520
import time


def main():
    n, p, q = map(int, input().split())
    A = list(map(int, input().split()))
    # A = [i for i in range(n)]
    # start = time.time()
    A = [a % p for a in A]
    ans = 0
    for i1 in range(n):
        for i2 in range(i1 + 1, n):
            for i3 in range(i2 + 1, n):
                for i4 in range(i3 + 1, n):
                    prod = A[i1]*A[i2]*A[i3]*A[i4]
                    prod %= p
                    for i5 in range(i4 + 1, n):
                        if (prod*A[i5]) % p == q:
                        # if (A[i1]*A[i2]*A[i3]*A[i4]*A[i5]) % p == q:
                            ans += 1

    # elapsed_time = time.time() - start
    # print(elapsed_time)
    print(ans)


main()

import sys


def main():
    n, p, q = map(int, input().split())
    A = [int(i) for i in sys.stdin.readline().split()]
    B = [a % p for a in A]
    ans = 0
    for i1 in range(n):
        for i2 in range(i1+1, n):
            x2 = (B[i1]*B[i2]) % p
            for i3 in range(i2+1, n):
                x3 = (x2*B[i3]) % p
                for i4 in range(i3+1, n):
                    x4 = (x3*B[i4]) % p
                    for i5 in range(i4+1, n):
                        x5 = (x4*B[i5]) % p
                        if x5 % p == q:
                            ans += 1
    print(ans)


main()

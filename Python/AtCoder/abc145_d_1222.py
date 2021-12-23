import numpy as np
# https://atcoder.jp/contests/abc145/tasks/abc145_d
# (0, 0) -> (0, 0)
# (1, 2) -> (0, 3)
# (2, 1) -> (3, 0)
# に変換する行列は
# [-1.  2.]
# [ 2. -1.]


def main():
    mod = 10**9 + 7
    x, y = map(int, input().split())
    xy = np.array([[x], [y]])
    A = np.array([[-1, 2], [2, -1]])
    xy = A @ xy
    x, y = xy[0][0], xy[1][0]
    if x < 0 or y < 0:
        print(0)
        return
    if not(x % 3 == 0 and y % 3 == 0):
        print(0)
        return
    x //= 3
    y //= 3
    # (x+y)C(x)
    # aCb = a!/(b!(a-b)!)
    frac = [1]*(x+y+1)
    for i in range(1, x+y+1):
        frac[i] = frac[i-1]*i
        frac[i] %= mod
    ans = frac[x+y]*rev(frac[x], mod)*rev(frac[y], mod)
    ans %= mod
    print(ans)


def rev(val, mod):
    return pow(val, mod-2, mod)

def test():
    A = np.array([[1, 2], [2, 1]])
    A_inv = np.linalg.inv(A)
    A_inv *= 3
    for a in A_inv:
        print(a)

main()

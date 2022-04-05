def main():
    n = int(input())
    # aは10**6が上限
    # aを決め打ちして、bを二分探索
    ans = float('inf')
    for a in range(10**6+1):
        if f(a, 0) > n:
            ans = min(ans, f(a, 0))
            break
        # f(a, b) >= nとなる、最小のbを求める
        ok = 10**6+1
        ng = -1
        while abs(ng - ok) > 1:
            mid = (ok + ng) // 2
            if f(a, mid) >= n:
                ok = mid
            else:
                ng = mid
        ans = min(ans, f(a, ok))
    print(ans)


def f(a, b):
    return a**3 + a**2*b + a*b**2 + b**3


main()

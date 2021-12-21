def main():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))

    def div_up(a, b):
        return (a + b - 1) // b

    def check(x):
        # k以下の切断で、全ての長さをx以下にできるか
        # 小いxが来ると、SUM(A)だけ時間がかかってしまいTLE
        # kが10**9オーダーなので、cntを数え上げるのはだめ
        cnt = 0
        for a in A:
            if a > x:
                # aを長さxで切り分ける
                # 切り上げ除算-1
                cnt += div_up(a, x)-1
        return cnt <= k

    # 二分探索
    ok = max(A)
    ng = 0
    while ok-ng > 1:
        mid = (ok+ng)//2
        if check(mid):
            ok = mid
        else:
            ng = mid
        # print(mid, check(mid))
    print(ok)


main()

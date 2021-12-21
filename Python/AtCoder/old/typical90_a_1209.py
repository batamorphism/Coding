# 答えで二分探索


def main():
    n, l = map(int, input().split())
    k = int(input())
    A = [0] + list(map(int, input().split())) + [l]
    # Aのn+1区分の長さをBとする
    B = []
    for i0, a0 in enumerate(A[:-1]):
        a1 = A[i0 + 1]
        B.append(a1 - a0)

    # Bをx以上になるように分割して、k+1個以上にできるか
    def check(x):
        cnt = 0
        sum_b = 0
        for b in B:
            sum_b += b
            if sum_b >= x:
                # ここまでで一個のピースになる
                cnt += 1
                sum_b = 0
        return cnt >= k + 1

    ok = 1
    ng = l+1
    while ng-ok > 1:
        mid = (ok+ng) // 2
        if check(mid):
            ok = mid
        else:
            ng = mid
    print(ok)


main()

# 答えで二分探索

def main():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))

    def check(x):
        # x個のプロジェクトを作ることができるか
        # min(a_i, x)の合計が、x*k以上であれば作れる
        return sum(min(a, x) for a in A) >= x * k

    ok = 0
    ng = sum(A)+1
    while ng - ok > 1:
        mid = (ok+ng) // 2
        if check(mid):
            ok = mid
        else:
            ng = mid
    print(ok)


main()

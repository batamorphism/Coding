# 答えで2分探索
def main():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))

    def check(val):
        # k回切った時の、最も長い丸太の長さをval以下にできるか
        cnt = 0
        for a_i in A:
            cnt += (a_i+val-1) // val - 1
            if cnt > k:
                return False
        return True

    ok = max(A)+1
    ng = 0
    while ok - ng > 1:
        mid = (ok+ng) // 2
        if check(mid):
            ok = mid
        else:
            ng = mid
    print(ok)


main()

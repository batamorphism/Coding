# 答えで二分探索
def main():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))

    def check(mid):
        # mid個以上のプロジェクトを作成できるか
        # 一つのプロジェクトにつき、各部署から1人しか選出できないので
        # mid人以上いる部署は無駄
        B = [min(a, mid) for a in A]
        # プロジェクト数*k人 <= 使える人数
        # であれば十分
        return mid*k <= sum(B)

    ok = 0
    ng = sum(A) + 1
    while ng - ok > 1:
        mid = (ok+ng)//2
        if check(mid):
            ok = mid
        else:
            ng = mid
    print(ok)


main()

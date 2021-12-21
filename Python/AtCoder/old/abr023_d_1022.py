INF = 10**10*10**5


def main():
    n = int(input())
    target_list = [tuple(map(int, input().split())) for _ in range(n)]

    def check(score):
        # score点が獲得しうるか
        # 全てのtargetを、(score-h)//s秒以内に破壊しなければならない
        limit_list = [(score-h)//s for h, s in target_list]
        limit_list.sort()
        for time, limit in enumerate(limit_list):
            if time > limit:
                return False
        return True

    ok = INF
    ng = -1
    while ok-ng > 1:
        mid = (ok+ng)//2
        if check(mid):
            ok = mid
        else:
            ng = mid
    print(ok)


main()

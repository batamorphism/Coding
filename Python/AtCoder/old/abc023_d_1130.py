# 答えで二分探索
def main():
    n = int(input())
    item_list = [tuple(map(int, input().split())) for _ in range(n)]

    def check(score):
        # scoreが達成できるか
        # (score-h_i) // s_i 秒以内に風船を割る必要がある
        need_sec_list = []
        for h_i, s_i in item_list:
            sec_i = (score-h_i) // s_i
            need_sec_list.append(sec_i)
        need_sec_list.sort()
        for sec, need in enumerate(need_sec_list):
            if need < sec:
                return False
        return True

    # checkがTrueとなる最小のscoreを探す
    lo = -1
    hi = 10**18
    while hi > lo:
        mid = (hi+lo) // 2
        if check(mid):
            hi = mid
        else:
            lo = mid
            lo += 1
    print(lo)


main()

import sys
sys.setrecursionlimit(10 ** 6)


def main():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    # 各a_iが何回呼ばれるかを評価する
    # nが小さいので、周期性を使う
    val_of = {}  # 今の飴の個数(mod n)における、操作回数と現在の総数のペア
    val = 0
    x = 0

    def solve(pre_i, pre_val, cur_i, cur_val, k, x):
        remain = k - cur_i - 1
        period = cur_i - pre_i
        loop = remain // period
        ans = cur_val + loop * (cur_val-pre_val)
        remain = remain % period
        for _ in range(remain):
            ans += A[x]
            x += A[x]
            x %= n
        print(ans)

    for i in range(k):
        val += A[x]
        x = (x + A[x]) % n
        if x in val_of:
            # 周期性が発覚
            pre_i, pre_val = val_of[x]
            cur_i, cur_val = i, val
            solve(pre_i, pre_val, cur_i, cur_val, k, x)
            return
        val_of[x] = (i, val)

    print(val)


main()

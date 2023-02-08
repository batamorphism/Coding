# 答えで二分探索
def main():
    n, x = map(int, input().split())
    k = int(input())
    A = list(map(int, input().split()))
    # Bを、各ピースの長さにする
    A = [0] + A + [x]
    B = []
    for i in range(1, len(A)):
        bef_i = i - 1
        aft_i = i
        B.append(A[aft_i]-A[bef_i])

    # 切れ目をk個選んで
    # 最も短いものの長さを最大化したい

    def check(mid):
        # 長さmidで切り分けていき
        # 切れ目をk個選ぶことが可能か
        cnt = 0
        cur_len = 0
        for i, b_i in enumerate(B):
            cur_len += b_i
            if cur_len >= mid:
                cnt += 1
                cur_len = 0
        if cnt >= k+1:
            return True
        else:
            return False

    ok = -1
    ng = x
    while (ng-ok) > 1:
        mid = (ok+ng)//2
        if check(mid):
            ok = mid
        else:
            ng = mid

    print(ok)


main()

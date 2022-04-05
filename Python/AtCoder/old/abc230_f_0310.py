from collections import defaultdict
MOD = 998244353


# 数列の輪が0になった区間は、
# その前と後で同じになる
# したがって、足して0になった区間は、カウントしない
# 区切りを入れて、その区切りの間で総和をとることを考える
def main():
    n = int(input())
    A = list(map(int, input().split()))
    pos_of = defaultdict(lambda: -1)
    cnt_of = defaultdict(lambda: 0)

    sum_a = 0
    for i, a_i in enumerate(A):
        if i == 0:
            cnt_of[i] = 1
            continue
        bef_i = pos_of[sum_a]
        sum_a += a_i
        if bef_i == -1:
            # 足す前と、足す後で、2倍になる
            cnt_of[i] = 2*cnt_of[i-1]
        else:
            # 単に末尾にa_iをくっつけるパターン
            cnt = cnt_of[i-1]
            # a_iを足し合わせるパターン
            cnt += cnt_of[i-1] - cnt_of[bef_i]
            cnt_of[i] = cnt
        pos_of[sum_a] = i
    ans = cnt_of[n-1]
    print(ans)


main()

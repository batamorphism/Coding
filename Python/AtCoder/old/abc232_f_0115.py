# 入れ替えた後の状態が分かって居れば、操作1側のコストはすぐに求められる。
# cur_S = 既に確定させたAの要素
# cur_n = cur_Sの要素数
# cur_Sは、Sに入っている各要素aから遷移する
# pre_Sから、aをnに移動させるのにかかるコストを求め、
# aとb_nの差からxを求めると、追加でかかる費用になる
def main():
    n, x, y = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    INF = float('inf')

    ALL = 1 << n
    DP = [INF] * ALL
    DP[0] = 0

    for cur_S in range(1, ALL):
        cur_n = popcount(cur_S)-1
        for i in range(n):
            if not have(cur_S, i):
                continue
            pre_S = remove(cur_S, i)
            a = A[i]
            # aをcur_nに持ってくる
            # aを0に持ってくる回数と、cur_nを0に持ってくる回数の差が答え
            a_cnt = popcount(((1 << i)-1) & ~pre_S)
            cnt = a_cnt
            # print(cnt, a_cnt, n_cnt, bin(pre_S), i, cur_n)
            # ただし、pre_Sに含まれている要素はすでに使われている
            # pre_Sのうち、a以上cur_n以下の要素数分だけ、移動させる必要がない
            cost1 = cnt * y
            cost2 = abs(a-B[cur_n])*x
            dp = DP[pre_S] + cost1 + cost2
            DP[cur_S] = min(DP[cur_S], dp)

    print(DP[-1])


def have(S, a):
    return (S >> a) & 1


def remove(S, a):
    return S ^ (1 << a)


def popcount(S):
    return bin(S).count('1')


main()

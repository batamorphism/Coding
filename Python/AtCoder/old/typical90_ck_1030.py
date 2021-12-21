from collections import deque

INF = 10**6
mod = 10**9+7
bitend = 10**6
bitdata = [0]*(bitend+10)


def add(pos, x):
    pos += 1
    while pos < bitend:
        bitdata[pos] += x
        bitdata[pos] %= mod
        pos += pos & -pos


def getsum(pos):
    pos += 1
    ret = 0
    while pos > 0:
        ret += bitdata[pos]
        ret %= mod
        pos -= pos & -pos
    return ret


def reset():
    for i in range(len(bitdata)):
        bitdata[i] = 0


def main():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))

    # 座標圧縮
    A_dict = {a: i for i, a in enumerate(sorted(list(set(A))))}
    A = [A_dict[a] for a in A]

    # DP[i]:A[i]を右端に持つAの部分列で、転倒数がk以下となる最小のindex
    le_of = [0]*n
    cnt = 0
    # 右から尺取り法
    que = deque()
    for le in range(n-1, -1, -1):
        que.appendleft((le, A[le]))
        cnt += getsum(A[le]-1)  # 左に追加した値以下の数が転倒数として増加
        add(A[le], 1)
        while que and not (cnt <= k):
            ri, rm = que.pop()
            cnt -= (getsum(bitend)-getsum(rm))  # 右で削除した値以上の数が転倒数として減少
            add(rm, -1)
            le_of[ri] = le+1  # 一個前まではセーフ

    def under_k(le, ri):
        # Aの部分列[le, ri]の転倒数がk以下か判定する
        return le >= le_of[ri]

    reset()

    # DP
    # DP[i] = iまで見たときの、条件を満たす分割数
    # DP = [0]*n
    for ri in range(n):
        le = le_of[ri]
        # [le, ri]の間はどう区切っても転倒数k以下

        """
        dp = 0
        if le != 0:
            dp += DP[le-1]
        else:
            dp += 1
        for i in range(le, ri):
            dp += DP[i]
        DP[ri] = dp
        print(dp)
        """
        # [le-1, ri]の累積和をとりたい
        dp = 0
        if le != 0:
            dp = getsum(ri-1)-getsum(le-2)
        else:
            dp += 1
            dp += getsum(ri-1)-getsum(le-1)
        add(ri, dp)

    print((getsum(n-1)-getsum(n-2)) % mod)


main()

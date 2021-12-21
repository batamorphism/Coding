from collections import deque

bit_data = [0]*(2*10**5+10)
bit_end = 2*10**5+5
mod = 10**9+7


def add(pos, x):
    pos += 1
    while pos < bit_end:
        bit_data[pos] += x
        pos += pos & -pos


def getsum(pos):
    pos += 1
    ret = 0
    while pos > 0:
        ret += bit_data[pos]
        pos -= pos & -pos
    return ret


def main():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    A = [0] + A
    n_end = n+1
    # 座標圧縮
    A_dict = {a: i for i, a in enumerate(sorted(list(set(A))))}
    A_comp = [A_dict[a] for a in A]

    # j_st_of[i]Aのj_st文字目~i文字目の転倒数がk個以下となる、最小のj_st
    j_st_of = [0]*n_end
    # 尺取り法
    # 逆向きに開始
    que = deque()
    cnt = 0  # 転倒数
    ind = n_end
    for a in A_comp[::-1]:
        ind -= 1  # 現在、Aのind文字目を見ている
        que.appendleft((a, ind))
        add(a, 1)
        # 転倒数は、i<jかつA[i]>A[j]を満たすもの
        # 左端にaを足すと、queにaより小の要素がどれだけあるかが、転倒数の増加になる
        cnt += getsum(a-1)
        while que and not cnt <= k:
            rm, rm_ind = que.pop()
            add(rm, -1)
            # 右端からrmを取り除くと、queにrmより大の要素がどれだけあるかが、転倒数の減少になる
            cnt -= len(que)-getsum(rm)
            j_st_of[rm_ind] = ind+1  # 1文字前まではセーフだった

    # 左端まで見ても大丈夫だった奴らの処理
    while que:
        rm, rm_ind = que.pop()
        j_st_of[rm_ind] = 1

    # DP
    cumsum = [0]*n_end
    DP = [0]*n_end
    DP[0] = 1
    cumsum[0] = 1
    for i in range(1, n_end):
        # 以下を高速化
        # for j in range(j_st_of[i]-1, i):
        #    DP[i] += DP[j]
        if j_st_of[i]-2 >= 0:
            DP[i] = cumsum[i-1]-cumsum[j_st_of[i]-2]
        else:
            DP[i] = cumsum[i-1]
        DP[i] %= mod
        cumsum[i] = (cumsum[i-1]+DP[i]) % mod

    print(DP[-1])


main()

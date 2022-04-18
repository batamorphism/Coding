def main():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))

    # 座標圧縮
    zipper = {a_i: i for i, a_i in enumerate(sorted(set(A)))}
    A = [zipper[a_i] for a_i in A]

    # Aをスワップさせて、先頭k個の総和をs+1以上とする

    A1 = A[:k]
    A2 = A[k:]

    # A1の各要素a_iについて
    # A2の中でa_iより大きいもののうち、インデックスが最も小さいものを選べばよい
    # sorted_set
    INF = float('inf')
    seg_max = 1
    while seg_max <= n:
        seg_max <<= 1
    seg_max <<= 1
    seg_data = [INF]*(seg_max*2)

    def update(pos, x):
        pos += seg_max
        seg_data[pos] = min(x, seg_data[pos])
        pos //= 2
        while pos > 0:  # 一番下から上に登りながら更新
            seg_data[pos] = min(seg_data[pos*2], seg_data[pos*2+1])
            pos //= 2

    def query(le, ri=seg_max):
        # [le, ri)の最大値を求める
        ret = INF
        le += seg_max
        ri += seg_max
        while le < ri:
            if le % 2 != 0:
                ret = min(seg_data[le], ret)
                le += 1
            le //= 2
            if ri % 2 != 0:
                ret = min(seg_data[ri-1], ret)
                ri -= 1
            ri //= 2
        return ret

    for i, a_i in enumerate(A2):
        update(a_i+1, i)

    ans = INF
    for i, a_i in enumerate(A1):
        # a_iより大きいもののうち、インデックスが最小の者
        ind = query(a_i+2)
        # 必要なスワップ回数は
        # k-i-1回と
        # ind回と
        # 1回
        # (k-i) + ind
        cur_ans = k-i+ind
        ans = min(ans, cur_ans)
    if ans == INF:
        ans = -1
    print(ans)


main()

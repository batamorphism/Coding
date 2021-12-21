INF = 10**12
seg_max = 1 << 15
seg_data = [0]*(2*seg_max-1)


def update(k, a):
    # k番目の値(0-indexed)をaに変更
    k += seg_max-1
    seg_data[k] = a
    while k > 0:
        k = (k-1)//2
        seg_data[k] = max(seg_data[k*2+1], seg_data[k*2+2])


def query(a, b, k=0, le=0, ri=seg_max):
    # [a, b)の最大値を求める
    # 最初は、query(a, b, 0, 0, seg_max)
    if ri <= a or b <= le:
        return -INF
    if a <= le and ri <= b:
        return seg_data[k]
    else:
        vl = query(a, b, k*2+1, le, (le+ri)//2)
        vr = query(a, b, k*2+2, (le+ri)//2, ri)
        return max(vl, vr)


def del_data():
    for i in range(len(seg_data)):
        seg_data[i] = 0


def main():
    w, n = map(int, input().split())
    stuff_list = []
    for _ in range(n):
        stuff = tuple(map(int, input().split()))
        stuff_list.append(stuff)

    # DP[n][w]:= n番目の料理までみて、使った香辛料の合計がwであるときの価値の最大値
    # DP[n][w] = max(DP[n-1][w], DP[n-1][w-le]+v～DP[n-1][w-ri]+v)
    # RangeMaxQuery
    le, ri, val = stuff_list[0]
    for wei in range(le, ri+1):
        update(wei, val)

    for i, stuff in enumerate(stuff_list[1:]):
        le, ri, val = stuff
        DP = [-INF]*(w+1)
        for wei in range(w+1):
            DP[wei] = max(query(wei, wei+1), query(max(wei-ri, 0), max(wei-le, 0)+1)+val)
        del_data()
        update(0, 0)
        for wei in range(w+1):
            update(wei, DP[wei])

    if DP[w] < 0:
        print(-1)
    else:
        print(DP[w])


main()

import sys
sys.setrecursionlimit(10**6)

bit_end = 10**5*2+10
bit_data = [0]*bit_end


def add(pos, x):
    pos += 1
    while pos < bit_end:
        bit_data[pos] += x
        pos += (pos & -pos)


def getsum(pos):
    pos += 1
    ret = 0
    while pos > 0:
        ret += bit_data[pos]
        pos -= (pos & -pos)
    return ret


def main():
    length, q_end = map(int, input().split())
    C = []
    X = []
    for _ in range(q_end):
        c, x = map(int, input().split())
        C.append(c)
        X.append(x)

    # 座標圧縮
    X += [0, length]
    X_dict = {x: i for i, x in enumerate(sorted(set(X)))}
    X_revdict = {i: x for x, i in X_dict.items()}
    X = [X_dict[x] for x in X]

    # 0とlengthに切れ込みを入れる
    add(X_dict[0], 1)
    add(X_dict[length], 1)

    for q in range(q_end):
        c, x = C[q], X[q]
        if c == 1:
            add(x, 1)
        else:
            # x以下の切れ込みを探す
            cnt = getsum(x)
            # getsum(ok)=<cntとなる最小のokを探す
            le = bisect(cnt)
            # getsum(ok)<=cnt+1となる最小のokを探す
            ri = bisect(cnt+1)
            le, ri = X_revdict[le], X_revdict[ri]  # 座標圧縮している分戻す
            # print(cnt, le, ri)
            print(ri-le)


def bisect(x):
    ok = bit_end
    ng = -1
    while ok-ng > 1:
        mid = (ok+ng)//2
        if getsum(mid) >= x:
            ok = mid
        else:
            ng = mid
    return ok


main()


def main():
    L, Q = map(int, input().split())
    C = []
    X = []
    for _ in range(Q):
        c, x = map(int, input().split())
        C.append(c)
        X.append(x)

    X.append(0)
    X.append(L)
    # 座標圧縮
    lines = {x: i+1 for i, x in enumerate(sorted(set(X)))}
    rev_lines = {i+1: x for i, x in enumerate(sorted(set(X)))}
    lines_last = len(lines)
    BIT_MAX = lines_last+10
    BIT = [0]*(BIT_MAX+10)

    def add(pos, x):
        pos += 1
        while pos < BIT_MAX:
            BIT[pos] += x
            pos += pos & -pos

    def sum(pos):
        pos += 1
        ret = 0
        while pos > 0:
            ret += BIT[pos]
            pos -= pos & -pos
        return ret

    add(0, 1)
    add(lines_last, 1)
    for i in range(Q):
        pos = lines[X[i]]
        if C[i] == 1:
            add(pos, 1)
        else:
            # cnt: pos以下で切れ込みが入っている個数
            cnt = sum(pos)
            # sum(pos) >= cntとなる最小のposを求める
            for lr in ['l', 'r']:
                if lr == 'l':
                    tgt = cnt
                else:
                    tgt = cnt+1
                ok = lines_last
                ng = 0
                while ok-ng > 1:
                    mid = (ok+ng)//2
                    if sum(mid) >= tgt:
                        ok = mid
                    else:
                        ng = mid
                if lr == 'l':
                    left = ok
                else:
                    right = ok

            print(rev_lines[right]-rev_lines[left])


main()

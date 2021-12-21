bit_data = [0]*(10**6+10)
bit_end = 10**6+5


def add(pos, val):
    pos += 1
    while pos < bit_end:
        bit_data[pos] += val
        pos += pos & -pos


def getsum(pos):
    ret = 0
    pos += 1
    while pos > 0:
        ret += bit_data[pos]
        pos -= pos & -pos
    return ret


def main():
    L, Q = map(int, input().split())
    query = [list(map(int, input().split())) for _ in range(Q)]
    c_list = []
    for _, x in query:
        c_list.append(x)
    # 座標圧縮
    c_list.append(0)
    c_list.append(L)
    c_dict = {c: i for i, c in enumerate(sorted(list(set(c_list))))}
    c_revdict = {i: c for i, c in enumerate(sorted(list(set(c_list))))}
    d_list = [c_dict[c] for c in c_list]
    add(0, 1)
    add(c_dict[L], 1)
    for c, x in query:
        x_comp = c_dict[x]
        if c == 1:
            # cut wood
            add(x_comp, 1)
        else:
            # get wood
            cnt = getsum(x_comp)
            lower_bound_comp = bisect(cnt)
            lower_bound = c_revdict[lower_bound_comp]
            upper_bound_comp = bisect(cnt+1)
            upper_bound = c_revdict[upper_bound_comp]
            print(upper_bound-lower_bound)


def bisect(cnt):
    ok = -1
    ng = bit_end+1
    while ng-ok > 1:
        mid = (ok+ng)//2
        if getsum(mid) < cnt:
            ok = mid
        else:
            ng = mid
    return ok+1


main()

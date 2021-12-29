# imos
# 最大値
def main():
    n, c_end = map(int, input().split())
    items_of = [[] for _ in range(c_end)]
    for _ in range(n):
        s, t, c = map(int, input().split())
        c -= 1
        items_of[c].append((s, t))
    for items in items_of:
        items.sort()

    for i, items in enumerate(items_of):
        items_of[i] = join(items)

    A = [0]*(10**5 + 2)
    item_list = []
    for items in items_of:
        for s, t in items:
            item_list.append((s, t))
    # print(item_list)
    for s, t in item_list:
        A[s] += 1
        A[t+1] -= 1

    for i in range(1, len(A)):
        A[i] += A[i-1]

    ans = max(A)
    print(ans)


def join(items):
    # item = (s, t)のうち、s=tとなっているものをくっつける
    ret = []
    if not items:
        return ret
    cur_s, cur_t = items[0]
    for s, t in items[1:]:
        if s == cur_t:
            cur_t = t
            continue
        else:
            ret.append((cur_s, cur_t))
            cur_s = s
            cur_t = t
    ret.append((cur_s, cur_t))
    return ret


main()

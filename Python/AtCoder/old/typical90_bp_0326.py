# クエリ先読み
def main():
    n = int(input())
    q = int(input())
    query_list = []
    for _ in range(q):
        t, x, y, v = map(int, input().split())
        x -= 1
        y -= 1
        query_list.append((t, x, y, v))

    # クエリに応えられるか否かは、
    # xとyが連結か否かと同値
    # setup union find
    par = [i for i in range(n)]
    siz = [1] * n

    def find(x):
        if x == par[x]:
            return x
        par[x] = find(par[x])
        return par[x]

    def union(x, y):
        x = find(x)
        y = find(y)
        if x == y:
            return
        if siz[x] < siz[y]:
            x, y = y, x
        par[y] = x
        siz[x] += siz[y]
        siz[y] = 0

    def is_same(x, y):
        return find(x) == find(y)

    # クエリ先読み
    A = [None] * n
    for t, x, y, v in sorted(query_list, key=lambda x: x[1]):
        if t == 1:
            continue
        # A[x]+A[y] = v
        if A[x] is None and A[y] is None:
            A[x] = 0
            A[y] = v
        elif A[x] is None:
            A[x] = v - A[y]
        elif A[y] is None:
            A[y] = v - A[x]
        else:
            if A[x] + A[y] == v:
                continue
            print(A[x], A[y])
            raise 1

    for t, x, y, v in query_list:
        if t == 0:
            union(x, y)
        elif t == 1:
            if not is_same(x, y):
                print('Ambiguous')
                continue

            pre_a_x = A[x]
            cur_a_x = v
            delta_x = cur_a_x-pre_a_x
            if (x-y) % 2 == 0:
                delta_y = delta_x
            else:
                delta_y = -delta_x
            pre_a_y = A[y]
            cur_a_y = pre_a_y + delta_y
            print(cur_a_y)
        else:
            raise 2


main()

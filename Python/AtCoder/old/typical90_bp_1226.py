# クエリ先読み
# t == 0を先に読むことで、整数列Aの候補を作ることができる
# 答えが一通りに定まる条件は、x <-> y にedgeを張った木について、x, yが連結であること
import sys
sys.setrecursionlimit(10**6)


def main():
    n = int(input())
    q = int(input())
    query_list = []
    q0_list = []
    for _ in range(q):
        t, x, y, v = map(int, input().split())
        x -= 1
        y -= 1
        query_list.append((t, x, y, v))
        if t == 0:
            q0_list.append((x, y, v))

    # 先読み
    A = [0]*n
    q0_list.sort()
    for x, y, v in q0_list:
        # A[x] + A[y] = v
        A[y] = v - A[x]
    # print(A)

    # union find
    par = [i for i in range(n)]

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
        par[x] = y

    def same(x, y):
        return find(x) == find(y)

    for t, x, y, v in query_list:
        if t == 0:
            union(x, y)
            continue
        if same(x, y):
            # 答えが定まる場合
            real_a_x = v
            a_x = A[x]
            delta_a_x = real_a_x - a_x
            a_y = A[y]
            if abs(x-y) % 2 == 0:
                sign = 1
            else:
                sign = -1
            delta_a_y = sign * delta_a_x
            real_a_y = a_y + delta_a_y
            print(real_a_y)
        else:
            print('Ambiguous')


main()

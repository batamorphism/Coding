import sys
sys.setrecursionlimit(10**9)

par = [i for i in range(2*10**5+1)]


def find(x):
    if par[x] == x:
        return x
    par[x] = find(par[x])
    return par[x]


def union(x, y):
    x = find(x)
    y = find(y)
    par[x] = y


def same(x, y):
    return find(x) == find(y)


def main():
    # クラスカル法
    # 最小全域木で、C_iの合計が最小となるようなものを作成する
    # この時、取り除いた辺のコスト合計は最大化されている
    # ただし、コストが負の時は問答無用で最小全域木に辺を追加させる
    n, m = map(int, input().split())
    edge_list = []
    for _ in range(m):
        a, b, c = map(int, input().split())
        edge_list.append((c, a, b))
    edge_list.sort()

    ans = 0
    for edge in edge_list:
        c, a, b = edge
        if c <= 0:
            union(a, b)
            continue
        if not same(a, b):
            union(a, b)
            continue
        ans += c
    print(ans)


main()

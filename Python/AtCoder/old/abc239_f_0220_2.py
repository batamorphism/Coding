import pypyjit
import sys
sys.setrecursionlimit(10**6)
pypyjit.set_param('max_unroll_recursion=-1')


def main():
    node_end, m = map(int, input().split())
    D = list(map(int, input().split()))
    D_ = D[:]

    # UnionFind
    par = [i for i in range(node_end)]
    # Dとlen(useful[node])は一致する・・はず
    useful = [[] for _ in range(node_end)]
    for node in range(node_end):
        for _ in range(D[node]):
            useful[node].append(node)

    def find(x):
        if x == par[x]:
            return x
        par[x] = find(par[x])
        return par[x]

    def union(x, y):
        x = find(x)
        y = find(y)
        if x == y:
            raise  # セーフ
        # yを親にする
        # ここで、D[x] <= D[y]
        if not(D[x] <= D[y]):
            x, y = y, x
        fr = useful[x].pop()
        to = useful[y].pop()
        par[x] = y
        D[y] += D[x] - 2
        D[x] = 0
        # useful[x]をuseful[y]に追加
        for val in useful[x]:
            useful[y].append(val)
        useful[x] = []
        if len(useful[y]) != D[y]:
            raise  # ここはセーフ
        return fr, to

    def is_same(x, y):
        return find(x) == find(y)

    def get_d(x):
        x = find(x)
        if len(useful[x]) != D[x]:
            raise  # ここはセーフ
        return D[x]

    def show_all():
        # 全ての連結成分を表示する
        used = set()
        for node in range(node_end):
            x = find(node)
            if x not in used:
                used.add(x)
                yield x

    edge_list = []
    for _ in range(m):
        a, b = map(lambda x: int(x) - 1, input().split())
        edge_list.append((a, b))

    if sum(D) != 2*node_end-2:
        print(-1)
        return

    for a, b in edge_list:
        if is_same(a, b):
            print(-1)
            return
        d_a = get_d(a)
        d_b = get_d(b)
        if min(d_a, d_b) <= 0:
            print(-1)
            return
        union(a, b)

    great_que = []  # 足りない要素数が2以上のやつ
    lower_que = []  # 足りない要素数が1のやつ
    for node in show_all():
        d = get_d(node)
        if d == 1:
            lower_que.append(node)
        elif d >= 2:
            great_que.append(node)

    ans_list = []
    while great_que and lower_que:
        great = great_que.pop()
        lower = lower_que.pop()
        fr, to = union(great, lower)
        ans_list.append((fr+1, to+1))
        great = find(great)
        d = get_d(great)
        if d == 1:
            lower_que.append(great)
        elif d >= 2:
            great_que.append(great)

    if great_que:
        print(-1)
        return

    last_list = []
    for node in show_all():
        last_list.append((node, get_d(node)))
    if len(last_list) == 1:
        # 既に答えに達している
        if last_list[0][1] != 0:
            raise  # セーフ
        for a, b in ans_list:
            print(a, b)
        return
    if len(last_list) != 2:
        # 条件を満たすことは不可能
        print(-1)
        return
    if last_list[0][1] != 1 or last_list[1][1] != 1:
        print(-1)
        return
    # 最後の二つをくっつける
    fr, to = union(last_list[0][0], last_list[1][0])
    ans_list.append((fr+1, to+1))

    # 題意を満たしているか
    nei_of = [[] for _ in range(node_end)]
    for a, b in edge_list:
        nei_of[a].append(b)
        nei_of[b].append(a)
    for a, b in ans_list:
        nei_of[a-1].append(b-1)
        nei_of[b-1].append(a-1)
    for node in range(node_end):
        if len(nei_of[node]) != D_[node]:
            print(-1)
            return

    for a, b in ans_list:
        print(a, b)


main()

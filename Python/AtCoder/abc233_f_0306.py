import sys
sys.setrecursionlimit(10**6)


def main():
    node_end = int(input())
    P = list(map(lambda x: int(x)-1, input().split()))
    rev_P = [-1]*node_end
    for i, p_i in enumerate(P):
        rev_P[p_i] = i
    m = int(input())

    # setup union find
    par = [i for i in range(node_end)]
    siz = [1]*node_end

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
        if not(siz[x] <= siz[y]):
            x, y = y, x
        par[x] = y
        siz[y] += siz[x]
        siz[x] = 0

    def is_same(x, y):
        return find(x) == find(y)

    nei_of = [[] for _ in range(node_end)]
    for i in range(m):
        a, b = map(lambda x: int(x)-1, input().split())
        if is_same(a, b):
            continue
        nei_of[a].append((b, i))
        nei_of[b].append((a, i))
        union(a, b)

    done = [False]*node_end
    par_of = [None]*node_end
    ans_list = []

    def solve(root):
        # rootの部分木について、ソートを行う
        # dfsで通った順番にsub_treeに入れていく
        sub_tree = []
        par_of[root] = (root, -1)
        que = [root]
        while que:
            pre = que.pop()
            sub_tree.append(pre)
            done[pre] = True
            for cur, i in nei_of[pre]:
                if done[cur]:
                    continue
                que.append(cur)
                par_of[cur] = (pre, i)
        # dfsで最後に通ったノードからスワップしていく
        for node in reversed(sub_tree):
            # nodeの値がnodeになるようにする
            # スワップする対象は、rev_P[node]
            target = rev_P[node]
            if not is_same(node, target):
                return False
            # target -> nodeに向かうパスが答え
            path = calc_path(target, node, root, par_of)
            for fr, to, i in path:
                ans_list.append(i+1)
                P[fr], P[to] = P[to], P[fr]
                rev_P[P[fr]], rev_P[P[to]] = rev_P[P[to]], rev_P[P[fr]]
        return True

    for node in range(node_end):
        if not done[node]:
            collect = solve(node)
        if not collect:
            print(-1)
            return
        if P[node] != node:
            raise

    print(len(ans_list))
    print(*ans_list)


def calc_path(target, node, root, par_of):
    target_to_root = []
    node_to_root = []
    while not target == root:
        par_node, edge_i = par_of[target]
        target_to_root.append((target, par_node, edge_i))
        target = par_node

    while not node == root:
        par_node, edge_i = par_of[node]
        node_to_root.append((node, par_node, edge_i))
        node = par_node

    while True:
        if not target_to_root:
            break
        if not node_to_root:
            break
        if target_to_root[-1] != node_to_root[-1]:
            break
        target_to_root.pop()
        node_to_root.pop()

    target_to_node = target_to_root + node_to_root[::-1]
    return target_to_node


main()

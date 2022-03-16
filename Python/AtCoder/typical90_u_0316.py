import sys
sys.setrecursionlimit(10**6)
import pypyjit
pypyjit.set_param('max_unroll_recursion=-1')


def main():
    # 強連結成分分解
    node_end, edge_end = map(int, input().split())
    nei_of = [[] for _ in range(node_end)]
    rev_nei_of = [[] for _ in range(node_end)]
    for _ in range(edge_end):
        fr, to = map(lambda x: int(x)-1, input().split())
        nei_of[fr].append(to)
        rev_nei_of[to].append(fr)

    dfs2_node_list = []
    done = [False]*node_end
    # DFSの帰りがけに順番を付ける
    # 順番が大きい方が、中央に近い
    # 順番が大きい順に、DFSをし直す

    def dfs1(pre):
        done[pre] = True
        for cur in nei_of[pre]:
            if done[cur]:
                continue
            dfs1(cur)
        dfs2_node_list.append(pre)

    for node in range(node_end):
        if done[node]:
            continue
        dfs1(node)

    # 逆順にDFS
    done2 = [False]*node_end
    cnt_list = []

    def dfs2(root):
        que = [root]
        cnt = 0
        while que:
            pre = que.pop()
            done2[pre] = True
            cnt += 1
            for cur in rev_nei_of[pre]:
                if done2[cur]:
                    continue
                done2[cur] = True
                que.append(cur)
        return cnt

    for node in reversed(dfs2_node_list):
        if done2[node]:
            continue
        cnt = dfs2(node)
        cnt_list.append(cnt)

    ans = 0
    for cnt in cnt_list:
        ans += (cnt-1)*cnt//2
    print(ans)


main()

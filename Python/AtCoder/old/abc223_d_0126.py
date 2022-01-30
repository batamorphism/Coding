# a_i, b_iにedgeを張った時のトポロジカルソート
import heapq


def main():
    node_end, edge_end = map(int, input().split())
    nei_of = [[] for _ in range(node_end)]
    cnt_of = [0]*node_end  # 各nodeに入ってくるedgeの数
    for _ in range(edge_end):
        fr, to = map(lambda x: int(x)-1, input().split())
        cnt_of[to] += 1
        nei_of[fr].append(to)

    for nei in nei_of:
        nei.sort()

    # cnt_ofが0の者から順にトポロジカルソート
    que = [node for node in range(node_end) if cnt_of[node] == 0]
    heapq.heapify(que)
    topology_sort = []

    while que:
        pre = heapq.heappop(que)
        topology_sort.append(pre)
        for cur in nei_of[pre]:
            cnt_of[cur] -= 1
            if cnt_of[cur] != 0:
                continue
            heapq.heappush(que, cur)

    ans = [v+1 for v in topology_sort]
    if len(ans) == node_end:
        print(*ans)
    else:
        print(-1)


main()


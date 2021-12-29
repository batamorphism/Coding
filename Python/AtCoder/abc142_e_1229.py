# 宝箱を開けた状態の組み合わせは全部で2**12=4096通り
# bitDPか、ダイクストラか
# ダイクストラしてみる
import heapq as hp


def main():
    n, m = map(int, input().split())
    INF = 10**9
    ALL = 1 << n
    key_list = []
    for _ in range(m):
        cost, b = map(int, input().split())
        C = list(map(lambda x: int(x)-1, input().split()))
        to_bit = 0
        for to in C:
            to_bit |= 1 << to
        key_list.append((cost, to_bit))

    node_end = ALL
    st_node = 0
    en_node = ALL-1
    nei_of = [[] for _ in range(node_end)]  # nei_of[fr] = (cost, to)

    cost_of = {}
    for fr in range(node_end):
        for cost, to_bit in key_list:
            to_bit |= fr
            # ここで、to_bitの重複が多すぎてTLE
            cost_of[(fr, to_bit)] = min(cost_of.get((fr, to_bit), INF), cost)

    for key, cost in cost_of.items():
        fr, to = key
        nei_of[fr].append((cost, to))

    for nei in nei_of:
        nei.sort()  # コストは低いほうがお得

    """
    for fr, nei in enumerate(nei_of):
        for cost, to in nei:
            print(bin(fr), bin(to), cost)
    """

    # INF = float('inf')
    dist = [INF] * node_end
    que = [(0, st_node)]
    dist[0] = 0
    while que:
        pre_d, pre_node = hp.heappop(que)
        if pre_node == en_node:
            break
        if pre_d > dist[pre_node]:
            continue
        for cost, to_node in nei_of[pre_node]:
            cur_d = pre_d + cost
            if dist[to_node] > cur_d:
                dist[to_node] = cur_d
                hp.heappush(que, (cur_d, to_node))
    ans = dist[en_node]
    if ans == INF:
        ans = -1
    print(ans)


main()

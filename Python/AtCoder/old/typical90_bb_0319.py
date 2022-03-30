from collections import deque


# 完全グラフはスターグラフに
def main():
    human_end, book_end = map(int, input().split())
    node_end = human_end + book_end

    def get_human_node(ind):
        return ind

    def get_book_node(ind):
        return human_end + ind

    nei_of = [[] for _ in range(node_end)]
    for book_ind in range(book_end):
        _ = int(input())
        R = list(map(lambda x: int(x)-1, input().split()))
        book_node = get_book_node(book_ind)
        human_node_list = [get_human_node(ind) for ind in R]
        # book_nodeとhuman_node_listをつなぐ
        for human_node in human_node_list:
            nei_of[human_node].append(book_node)
            nei_of[book_node].append(human_node)

    # 0からの距離を求める
    # BFS
    INF = float('inf')
    dist = [INF]*node_end
    dist[0] = 0
    que = deque([0])
    while que:
        pre = que.popleft()
        pre_d = dist[pre]
        cur_d = pre_d + 1
        for cur in nei_of[pre]:
            if dist[cur] <= cur_d:
                continue
            dist[cur] = cur_d
            que.append(cur)

    # write ans
    for human in range(human_end):
        human_ind = get_human_node(human)
        ans = dist[human_ind]
        if ans == INF:
            ans = -1
        else:
            ans //= 2
        print(ans)


main()

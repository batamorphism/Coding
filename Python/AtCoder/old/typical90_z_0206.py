from collections import deque


# 二部グラフの判定
def main():
    node_end = int(input())
    nei_of = [[] for _ in range(node_end)]

    for _ in range(node_end-1):
        a, b = map(lambda x: int(x)-1, input().split())
        nei_of[a].append(b)
        nei_of[b].append(a)

    # 0, 1で色を付ける
    col = [-1]*node_end
    col[0] = 0
    que = deque([0])
    while que:
        pre = que.popleft()
        cur_col = col[pre] ^ 1
        for cur in nei_of[pre]:
            if col[cur] == -1:
                # 着色処理
                col[cur] = cur_col
                que.append(cur)
            else:
                # 色チェック
                if col[cur] != cur_col:
                    raise
                continue

    col0_node_list = [node for node, col in enumerate(col) if col == 0]
    col1_node_list = [node for node, col in enumerate(col) if col == 1]
    if len(col0_node_list) >= len(col1_node_list):
        ans_list = col0_node_list
    else:
        ans_list = col1_node_list

    ans_list = ans_list[:node_end//2]
    ans_list = [a+1 for a in ans_list]
    print(*ans_list)


main()

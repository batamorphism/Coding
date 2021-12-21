from collections import deque
# head nodeからの距離が偶数のものを0で塗る
# これでよい
def main():
    node_end = int(input())
    nei_of = [[] for _ in range(node_end)]

    # 距離はmod2で考えてよい
    for _ in range(node_end - 1):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        w %= 2
        nei_of[u].append((v, w))
        nei_of[v].append((u, w))

    color = [-1]*node_end
    # -1:未定義、0:白、1:黒

    que = deque()
    que.append(0)
    color[0] = 0
    while que:
        pre = que.popleft()
        pre_color = color[pre]
        for cur, w in nei_of[pre]:
            if color[cur] == -1:
                color[cur] = pre_color ^ w
                que.appendleft(cur)

    print(*color)


main()

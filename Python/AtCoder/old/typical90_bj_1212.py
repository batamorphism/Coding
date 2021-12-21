# 逆向きに考える
# 全てのボールが黒くなっているとき
# a_i, b_i のどちらか一方がiの時、白に戻せる
# いくつかのボールが白くなっているとき
# a_i, b_iのどちらかが白いか、iの時、iを白に戻せる
from collections import deque


def main():
    n = int(input())
    ans_list = deque()

    AB = []
    for _ in range(n):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        AB.append((a, b))

    color = ['w'] * n
    que = deque()
    for i, ab in enumerate(AB):
        if i in ab:
            que.append(i)
            color[i] = 'b'

    # nei_of[node]で、a_i -> iとb_i -> iを返す
    nei_of = [[] for _ in range(n)]
    for i, ab in enumerate(AB):
        a, b = ab
        if a != i:
            nei_of[a].append(i)
        if b != i:
            nei_of[b].append(i)

    while que:
        pre = que.popleft()
        ans_list.appendleft(pre)
        for cur in nei_of[pre]:
            if color[cur] == 'w':
                que.append(cur)
                color[cur] = 'b'

    if len(ans_list) != n:
        print(-1)
        return

    for ans in ans_list:
        print(ans + 1)


main()

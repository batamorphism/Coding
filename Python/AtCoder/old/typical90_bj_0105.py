from collections import deque


# 後ろから考える
# 最後はすべてのボールが黒い
# あるボールiを白くするためには、i自身へのedgeがあるか、隣接ノード(a, b)のいずれかが白いことが条件
# これは、a, bのいずれかが白であった場合、iを白くできる
# これで、全体を白くできるか
def main():
    n = int(input())
    nei_of = [[] for _ in range(n)]
    que = deque()
    ans = deque()
    color = [1]*n
    for i in range(n):
        a, b = map(lambda x: int(x) - 1, input().split())
        nei_of[a].append(i)
        nei_of[b].append(i)
        if a == i or b == i:
            que.append(i)
            ans.appendleft(i)
            color[i] = 0

    # i -> iとなっているnodeをqueに追加し、ansにedgeを追加

    while que:
        pre = que.popleft()
        if color[pre] == 1:
            raise
        for cur in nei_of[pre]:
            # curが黒なら、preがすでに白なので、白くできうる
            if color[cur] == 1:
                color[cur] = 0
                ans.appendleft(cur)
                que.append(cur)

    if max(color) == 1:
        print(-1)
        return

    for a in ans:
        print(a+1)


main()

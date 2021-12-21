from collections import deque
# i -> A[i]に話が伝わる
# つまり、i->A[i]の有向のedge


def main():
    n, x = map(int, input().split())
    nei_of = [[] for _ in range(n)]
    A = list(map(int, input().split()))
    for i, a in enumerate(A):
        nei_of[i].append(a-1)

    # dfs
    que = deque()
    que.append(x-1)
    ans = 1
    color = ['w']*n
    color[x-1] = 'b'
    while que:
        pre = que.popleft()
        for cur in nei_of[pre]:
            if color[cur] == 'w':
                color[cur] = 'b'
                que.append(cur)
                ans += 1

    print(ans)


main()

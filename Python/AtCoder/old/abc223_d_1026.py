from collections import deque
import heapq as hq

def main():
    # トポロジカルソート
    n, m = map(int, input().split())
    super_node = n
    nei_of = [[] for _ in range(n+1)]
    # a -> bのedgeを張ってトポロジカルソートする
    cnt_in = [0]*n
    for _ in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        nei_of[a].append(b)
        cnt_in[b] += 1

    # cnt_in = 0のものが複数あるので、super_nodeからedgeを張る
    for node in range(n):
        if cnt_in[node] == 0:
            nei_of[super_node].append(node)
            cnt_in[node] += 1

    # トポロジカルソート
    que = []
    que.append(super_node)
    ans = []
    while que:
        pre_node = hq.heappop(que)
        ans.append(pre_node+1)
        for cur_node in nei_of[pre_node]:
            cnt_in[cur_node] -= 1
            if cnt_in[cur_node] == 0:
                hq.heappush(que, cur_node)

    if [cnt for cnt in cnt_in if cnt != 0]:
        print(-1)
    else:
        print(*ans[1:])


main()

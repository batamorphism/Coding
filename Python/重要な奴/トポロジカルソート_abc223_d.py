import heapq


def main():
    n, m = map(int, input().split())
    nei_of = [[] for _ in range(n)]
    in_cnt = [0]*n
    for _ in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        nei_of[a].append(b)
        in_cnt[b] += 1
    for num in nei_of:
        num.sort()

    # トポロジカルソート
    que = [i for i in range(n) if in_cnt[i] == 0]
    heapq.heapify(que)
    ans = []
    while que:
        pre_node = heapq.heappop(que)
        ans.append(pre_node)
        for cur_node in nei_of[pre_node]:
            in_cnt[cur_node] -= 1
            if in_cnt[cur_node] == 0:
                heapq.heappush(que, cur_node)

    if sum(in_cnt) > 0:
        print(-1)
    else:
        ans = [a+1 for a in ans]
        print(*ans)


main()

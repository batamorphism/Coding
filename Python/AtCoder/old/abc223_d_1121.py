import heapq as hp

# トポロジカルソート
def main():
    n, m = map(int, input().split())
    nei_of = [[] for _ in range(n)]
    cnt_in = [0]*n
    for _ in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        # a -> bのedgeが張られたグラフをトポロジカルソートする
        # ただしDAG出ない場合は-1
        nei_of[a].append(b)
        cnt_in[b] += 1

    # トポロジカルソート
    ans = []
    que = []
    for node, cnt in enumerate(cnt_in):
        if cnt == 0:
            hp.heappush(que, node)  # 辞書順最小なので、heapqueを使う

    while que:
        pre = hp.heappop(que)
        ans.append(pre)
        for cur in nei_of[pre]:
            cnt_in[cur] -= 1
            if cnt_in[cur] == 0:
                hp.heappush(que, cur)

    if len(ans) != n:
        print(-1)
        return

    ans = [a+1 for a in ans]
    print(*ans)


main()

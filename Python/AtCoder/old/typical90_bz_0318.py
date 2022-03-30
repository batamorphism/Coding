def main():
    node_end, edge_end = map(int, input().split())
    nei_of = [[] for _ in range(node_end)]
    for _ in range(edge_end):
        fr, to = map(lambda x: int(x)-1, input().split())
        nei_of[fr].append(to)
        nei_of[to].append(fr)

    ans = 0
    for node in range(node_end):
        cnt = 0
        for nei in nei_of[node]:
            if nei < node:
                cnt += 1
                if cnt >= 2:
                    break
        if cnt == 1:
            ans += 1

    print(ans)


main()

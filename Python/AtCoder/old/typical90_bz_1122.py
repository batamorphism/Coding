def main():
    # 各隣接リストnei_of[node]について、node以下の点がちょうど1つかどうか
    # つまり、nei_of[node]をsortしておいて、最小のものがnodeより小さく、
    # 2番目が存在しないかnodeより大
    n, m = map(int, input().split())
    nei_of = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        nei_of[a].append(b)
        nei_of[b].append(a)

    for neighbor in nei_of:
        neighbor.sort()

    ans = 0
    for node, nei in enumerate(nei_of):
        # len(nei) == 0は存在しない。
        if len(nei) == 1 and nei[0] < node:
            ans += 1
            continue
        if nei[0] < node and nei[1] > node:
            ans += 1

    print(ans)


main()

# DP
def main():
    MOD = 998244353
    node_end, edge_end, k = map(int, input().split())
    nei_of = [set() for _ in range(node_end)]
    for _ in range(edge_end):
        fr, to = map(lambda x: int(x) - 1, input().split())
        nei_of[fr].add(to)
        nei_of[to].add(fr)

    # 現在、nodeに居る状態における、旅の個数
    DP = [0]*node_end
    DP[0] = 1

    # 配るDP
    for i in range(k):
        new_DP = [0]*node_end
        # 橋が壊れていなかったとしたら、どのnodeからもcurに来れる
        sum_ = sum(DP) % MOD
        for cur in range(node_end):
            new_DP[cur] = sum_ - DP[cur]  # 移動しないことは許さない

        # 橋が壊れている分、減算
        for pre in range(node_end):
            for cur in nei_of[pre]:  # O(5000)
                new_DP[cur] -= DP[pre]

        for node in range(node_end):
            DP[node] = new_DP[node] % MOD

    ans = DP[0]
    print(ans)


main()

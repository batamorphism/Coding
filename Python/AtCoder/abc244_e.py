def main():
    MOD = 998244353
    node_end, edge_end, k, st, en, x = map(int, input().split())
    st -= 1
    en -= 1
    x -= 1

    # DP[node][0]  現在nodeに居て、、xが偶数回置換された状態
    # DP[i][1]  現在nodeに居て、xが奇数回置換された状態

    nei_of = [[] for _ in range(node_end)]
    for _ in range(edge_end):
        fr, to = map(lambda x: int(x)-1, input().split())
        nei_of[fr].append(to)
        nei_of[to].append(fr)

    DP = [[0]*2 for _ in range(node_end)]
    # stの処理
    if st == x:
        DP[st][1] = 1
    else:
        DP[st][0] = 1

    # 1, ..., k-1まで
    for cur_i in range(1, k):
        new_DP = [[0]*2 for _ in range(node_end)]
        for cur_node in range(node_end):
            for nex_node in nei_of[cur_node]:
                if nex_node == x:
                    new_DP[nex_node][1] += DP[cur_node][0]
                    new_DP[nex_node][0] += DP[cur_node][1]
                else:
                    new_DP[nex_node][0] += DP[cur_node][0]
                    new_DP[nex_node][1] += DP[cur_node][1]
        for node in range(node_end):
            for flg in range(2):
                DP[node][flg] = new_DP[node][flg] % MOD

    # enの処理
    ans = 0
    for pre_node in nei_of[en]:
        if en == x:
            ans += DP[pre_node][1]
        else:
            ans += DP[pre_node][0]
    ans %= MOD
    print(ans)


main()

# 小さい数からみていく
# 各マス毎に、最大何回移動できるかカウントしていく
# 各行、列ごとに、最大何回移動できるか記録しておく
# そのあと、更新しなおす
def main():
    r_end, c_end, n = map(int, input().split())
    rca = []
    for i in range(n):
        r, c, a = map(int, input().split())
        r -= 1
        c -= 1
        rca.append((r, c, a, i))

    rca.sort(key=lambda x: x[2], reverse=True)
    # DP_R[r]各行における最大移動回数
    INF = float('inf')
    DP_R = [-INF]*r_end
    DP_C = [-INF]*c_end
    query = []
    pre_a = -1
    ans = [0]*n
    for r, c, a, i in rca:
        if a != pre_a:
            # new_DP_R, new_DP_Cを更新
            pre_a = a
            for r_, c_, move in query:
                DP_R[r_] = max(DP_R[r_], move)
                DP_C[c_] = max(DP_C[c_], move)
            query = []
        move_c = DP_C[c] + 1
        move_r = DP_R[r] + 1
        move = max(move_c, move_r, 0)
        query.append((r, c, move))
        ans[i] = move

    for i in range(n):
        print(ans[i])


main()

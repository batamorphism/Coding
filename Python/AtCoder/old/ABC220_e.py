# https://atcoder.jp/contests/abc220/submissions/26113813
mod = 998244353
N, D = map(int, input().split())
pw = [0]*(N+D+1)
pw[0] = 1
for i in range(1, N+D+1):
    pw[i] = pw[i - 1] * 2 % mod
ans = 0

# 以下、i<jを仮定する
for depth in range(N):
    # lca の深さが depth

    # iがlcaそのものの時
    if depth+D < N:
        ans += pw[depth+D]
        ans %= mod

    # iがlcaではなく、lcaの左側と右側を考える必要がある場合
    # lcaの組み合わせ : 2^depth 個
    # 左の山 深さ depth + x     : 2^{x-1} 個
    # 右の山 深さ depth + D - x : 2^{D-x-1} 個
    # 合計　2^{D+depth-2} 個
    # ここでxは左の山が持つ辺の数(深さ)である

    # x の範囲は？
    # 0 < x < D (距離がDのため)
    # depth + x < N（左の山の深さが上限を突破しないこと）
    # depth + D - x < N (右の山の深さが上限を突破しないこと)
    # <-> depth + D - N < x < N - depth

    lo = max(1, depth+D-N+1)
    hi = min(D-1, N-depth-1)
    if lo > hi:
        continue

    ans += pw[D+depth-2] * (hi-lo+1)
    ans %= mod


print(ans * 2 % mod)

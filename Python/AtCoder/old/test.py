def solve():
  MOD = 998244353
  n = int(input())
  l = [-1] + [*map(lambda x:ord(x)-ord("A"), list(input()))]

  #dp[i][s][a, b] aはそのコンテストに出場しない場合 bはする場合
  dp = [[[1,0]]+[[0,0] for _ in [0]*((1<<10)-1)] for _ in [0]*(n+1)]

  for i in range(1, n+1):
    #x: 今回のコンテスト
    #xx: 前回のコンテスト
    x = l[i]
    xx = l[i-1]
    for j in range(1, 1<<10):
      #出場しない場合
      dp[i][j][0] += sum(dp[i-1][j])

      #集合にxが入ってる時のみ処理
      if (j>>x)&1:

        #xを抜いた集合
        jj = (1<<x)^j

        #初めて出場
        dp[i][j][1] += sum(dp[i-1][jj])

        #初めてじゃないけど出場
        if jj == 0:
          #コンテストの種類が１種類の場合
          dp[i][j][1] += sum(dp[i-1][j])
        elif x == xx:
          # <- 前回のコンテストに出場していない場合、前回出場したコンテストはxxになるとは限らない。
          # <- したがって、DPに、前回出場したコンテストを持たせる必要がある。
          #コンテストの種類が複数+前回と同じコンテスト
          dp[i][j][1] += dp[i-1][j][1]

      dp[i][j][0] %= MOD
      dp[i][j][1] %= MOD

  cnt = 0
  for pls in dp[-1][1:]:
    cnt += sum(pls)
    cnt %= MOD

  print(cnt)

if __name__ == '__main__':
  solve()
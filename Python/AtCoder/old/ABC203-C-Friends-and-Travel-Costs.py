# dp[n] := n人目の友達がいる街A[i]にたどり着けるか、また、たどり着きB[i]円を受け取った際の値段
# dp[n] == -1 の時、たどり着いていないものとする
# dp[n] = dp[n-1]が-1ならば、-1
# そうでないならば、dp[n-1] >= (A[n]-A[n-1]) である場合に限り
# dp[n] = dp[n-1] - (A[n] -A[n-1]) + B[i]
# こうしてdp[n]を作成していき、初めてdp[n] == -1となった時
# A[n-1] + dp[n-1]が答え


def main():
    n, k, *_AB = map(int, open(0).read().split())
    AB = [[0, 0] for i in range(n+1)]

    ans = 0
    for i in range(n):
        # A[i+1] = _AB[2*i]
        # B[i+1] = _AB[2*i+1]
        AB[i+1] = [_AB[2*i], _AB[2*i+1]]

    AB.sort()

    dp = [-1] * (n+1)

    dp[0] = k
    for nn in range(1, n+2):   # nnは1~n
        if nn == n+1:   # もう友だちがいない
            ans = AB[nn-1][0] + dp[nn-1]
            break
        elif dp[nn-1] == -1:
            # 死にロジック
            dp[nn] == -1
        elif dp[nn-1] >= AB[nn][0]-AB[nn-1][0]:
            dp[nn] = dp[nn-1]-(AB[nn][0]-AB[nn-1][0])+AB[nn][1]
        else:
            dp[nn] = -1
            ans = AB[nn-1][0] + dp[nn-1]
            break

    print(ans)


main()

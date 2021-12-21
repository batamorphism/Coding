def main():
    # input
    n = int(input())
    A = []
    for _ in range(n):
        a = int(input())
        A.append(a)

    # 区間DP
    DP = [[0]*n for _ in range(n)]
    # DP[left][right]
    # = ケーキがleftからrightまで残っているときの
    #   J君の取り分の最大値
    #   この状態がJ君とIちゃんのどっちのターンかは偶奇で決まる
    #   DP[i][i]はケーキが残ってないので、0
    # DP[0][1]は0, 1が残ってる
    # DP[1][0]は1, 2, ..., 0が残ってる（つまり全部
    # DP[1][1]は1だけが残ってる
    for i in range(1, n+1):
        # iは残っているケーキの数
        # すなわち、right=left+i-1 mod n
        for left in range(n):
            right = (left+i-1) % n
            if (n-i) % 2 == 0:  # 既に取ったケーキが2の倍数なので、J君のターン
                DP[left][right] = max(DP[(left+1) % n][right]+A[left],  # leftのケーキをとった場合
                                      DP[left][(right-1+n) % n]+A[right])  # rightのケーキをとった場合
            else:  # Iちゃんのターン
                if (A[left] > A[right]):
                    DP[left][right] = DP[(left+1) % n][right]
                else:
                    DP[left][right] = DP[left][(right-1+n) % n]

    ans = 0
    for i in range(n):
        ans = max(ans, DP[i][(i+n-1) % n])
    print(ans)


main()

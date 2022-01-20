from collections import defaultdict
MOD = 998244353


# 1 0 2 は 1+0, 2と 1, 0+2で重複する
# 重複を考えない場合
# i番目まで見たときの数列として考えられる数をDP[i]として
# DP[i] += DP[i-1] // i番目とi-1番目で和を取らない場合
# DP[i] += DP[i-1] // i番目とi-1番目で和を取る場合
# ここで、和を取る場合について、前述の重複が存在する
# A[j]+...+A[i] = 0となるjがあるとき
# DP[i]はDP[j]個だけ重複があるので、これを除く
def main():
    n = int(input())
    A = list(map(int, input().split()))
    # n = 3
    # A = [1, 0, 2]
    d = defaultdict(lambda: -1)
    DP = [0]*n

    DP[0] = 1  # 空集合
    sum_a = 0
    for i in range(1, n):
        DP[i] = 2*DP[i-1]
        # 重複を除く
        # A[i-1]までの和と一致するものを探す
        sum_a += A[i-1]
        j = d[sum_a]
        if j != -1:
            DP[i] -= DP[j]
        DP[i] %= MOD
        d[sum_a] = i-1

    print(DP[n-1])


main()

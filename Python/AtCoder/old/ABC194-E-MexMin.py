def main():
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    DP = [-1]*(n-m+1)
    # DP[0] = mex(A[0],...,A[m-1])
    # DP[n-m] = mex(A[n-m],...,A[n-1])
    # DP[1] = { DP[0]がA[

    # set DP[0]
    DP[0] = mex(A[0:m])

    # DP[1]からDP[n-m]を計算
    for i in range(1, n-m+1):
        pre_dp = 0
        if A[i-1] < DP[0]:  # 更新可能性あり
            pre_dp = mex(A[i:i+m-1])
        else:
            pre_dp = DP[i-1]

        if A[i+m-1] == pre_dp:
            DP[i] = mex(A[i:i+m])
        else:
            DP[i] = pre_dp

    DP.sort()
    print(DP[0])


def mex(A: list):
    if len(A) <= 0:
        return 1e14
    for i in range(len(A)+1):
        if i not in A:
            return i


main()

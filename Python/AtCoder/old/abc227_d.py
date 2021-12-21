def main():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))

    # p個以上のプロジェクトを作ることができるための条件
    # 各iについて、min(A[i], P)を足し合わせたものをsumとする
    # p*k<=sumの時はp個以上のプロジェクトを作ることができる
    # p*k>sumの時はできない

    def check(p):
        sum_ = 0
        for a in A:
            sum_ += min(a, p)
        return p * k <= sum_

    ok = 0
    ng = 10**18 // k
    while ng - ok > 1:
        mid = (ok + ng) // 2
        if check(mid):
            ok = mid
        else:
            ng = mid

    print(ok)


main()

def main():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))

    def check(num):
        # num個のプロジェクトを作れるか
        cnt = 0
        for a in A:
            cnt += min(a, num)
        return cnt >= k*num

    # 二分探索
    ok = 0
    ng = sum(A)+1

    while ng - ok > 1:
        mid = (ok + ng) // 2
        if check(mid):
            ok = mid
        else:
            ng = mid

    print(ok)


main()

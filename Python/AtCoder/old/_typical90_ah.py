def main():
    # N <= 10**5
    # 二分探索
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    ok = 1
    ng = n+1
    while ng-ok > 1:
        mid = (ok+ng)//2
        if check(A, mid, k):
            ok = mid
        else:
            ng = mid
    print(ok)


def check(A, x, k) -> bool:
    # Aの長さxの連続した部分列のうち、
    # 要素がk種類以下のものが存在する
    # 尺取り法
    dic = {}
    for a in A[:x]:
        dic[a] = dic.get(a, 0)+1
    left_end = len(A)-x
    if len(dic) <= k:
        return True

    for left in range(left_end):
        right = left+x
        # remove_left
        dic[A[left]] -= 1
        if dic[A[left]] == 0:
            del dic[A[left]]
        dic[A[right]] = dic.get(A[right], 0)+1
        if len(dic) <= k:
            return True

    return False


main()

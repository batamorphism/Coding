def main():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    for _ in range(k):
        A = one_step(A)
        if len(list(a for a in A if a == n)) == n:
            # 定常状態
            break
    print(*A)


def one_step(A):
    n = len(A)
    ret = [0]*n
    for i, a_i in enumerate(A):
        # i-a_i～i+a_iに+1
        lo = max(0, i-a_i)
        hi = min(n-1, i+a_i)
        ret[lo] += 1
        if hi + 1 < n:
            ret[hi+1] -= 1
    for i in range(1, n):
        ret[i] += ret[i-1]
    return ret


main()

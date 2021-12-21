def main():
    n, k = map(int, input().split())
    A = [0] + [int(input()) for _ in range(n)]

    for i in range(1, n + 1):
        A[i] += A[i - 1]

    for i in range(n + 1):
        A[i] -= k*i

    # 0 <= le < ri <= nについて
    # A[le] <= A[ri]となるペアを求める
    # complex A
    A_zipper = {a: i for i, a in enumerate(sorted(set(A)))}
    A = [A_zipper[a] for a in A]
    bit_end = n + 10
    bit_data = [0] * bit_end

    def add(pos, val):
        pos += 1
        while pos < bit_end:
            bit_data[pos] += val
            pos += (pos & -pos)

    def getsum(pos):
        ret = 0
        pos += 1
        while pos > 0:
            ret += bit_data[pos]
            pos -= (pos & -pos)
        return ret

    # setup bit
    ans = 0
    for ri, a_ri in enumerate(A):
        cnt = getsum(a_ri)
        add(a_ri, 1)
        ans += cnt

    print(ans)


main()

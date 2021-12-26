def main():
    n, q = map(int, input().split())
    A = list(map(int, input().split()))
    # 不便さは、Aの差分からなる配列をBとして
    # sum(abs(B))となる
    # [le, ri]に+vする操作は
    # B[le-1]に+v
    # B[ri]に-v
    # と対応する
    B = []
    for i, a_i in enumerate(A[:-1]):
        a_j = A[i+1]
        B.append(a_j - a_i)

    ans = sum(abs(b) for b in B)
    ans_list = []
    for _ in range(q):
        le, ri, v = map(int, input().split())
        le -= 1
        ri -= 1
        # 答えの変動量を求める
        delta_ans = 0
        if le-1 >= 0:
            delta_ans += abs(B[le-1] + v) - abs(B[le-1])
            B[le-1] += v
        if ri < n-1:
            delta_ans += abs(B[ri] - v) - abs(B[ri])
            B[ri] -= v
        ans += delta_ans
        ans_list.append(ans)

    print(*ans_list, sep='\n')


main()

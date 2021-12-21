def main():
    # 地殻変動で不便さが変わるのは、
    # le-1 -> le
    # ri -> ri+1
    # の2箇所のみ
    # A[i+1]-A[i]からなる配列Bを考える
    # [le, ri]に+valされることは
    # B[le-1] += val, B[ri] -= valと同値
    # ここで不便さは、SUM(abs(B))となる
    # 一回の操作で、abs(B[le])とabs(B[ri+1])が増えた量をdel_valとすると
    # 毎回の操作でdel_valだけ答えが変わっていくこととなる

    # input
    n, q = map(int, input().split())
    A = list(map(int, input().split()))
    query_list = []
    for _ in range(q):
        le, ri, val = map(int, input().split())
        le -= 1
        ri -= 1
        query_list.append((le, ri, val))

    B = [0] * (n)
    for i in range(n-1):
        B[i] = A[i+1]-A[i]

    # 初期値を求める
    ans = 0
    for b in B:
        ans += abs(b)

    # print(ans, B)

    for le, ri, val in query_list:
        if le == 0:
            bef_le = 0
            aft_le = 0
        else:
            bef_le = B[le-1]
            B[le-1] += val
            aft_le = B[le-1]
        if ri == n-1:
            bef_ri = 0
            aft_ri = 0
        else:
            bef_ri = B[ri]
            B[ri] -= val
            aft_ri = B[ri]
        del_ans = abs(aft_le) + abs(aft_ri) - abs(bef_le) - abs(bef_ri)
        ans += del_ans
        print(ans)


main()

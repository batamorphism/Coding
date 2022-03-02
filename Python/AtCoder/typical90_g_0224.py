# 貪欲
def main():
    n = int(input())
    INF = float('inf')
    A_ = list(map(int, input().split()))
    A = []
    for i, a_i in enumerate(A_):
        A.append((a_i, 'a', i))
    A.append((INF, 'a', n))

    q = int(input())
    B = []
    for i in range(q):
        b = int(input())
        B.append((b, 'b', i))

    AB = A+B
    AB.sort()

    pre_a = -INF
    b_list = []
    ans = [0]*q
    for ab in AB:
        if ab[1] == 'a':
            nex_a = ab[0]
            for b_i, i in b_list:
                cur_score = min(abs(nex_a - b_i), abs(pre_a - b_i))
                ans[i] = cur_score
            pre_a = nex_a
            b_list = []
        else:
            b_list.append((ab[0], ab[2]))

    for a in ans:
        print(a)


main()

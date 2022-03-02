def main():
    t = int(input())
    ans_list = []
    for _ in range(t):
        n, m = map(int, input().split())
        case = [tuple(map(int, input().split())) for _ in range(n)]
        ans = solve(n, m, case)
        ans_list.append(ans)

    for ans in ans_list:
        print(ans)


def solve(n, m, case):
    # 各B[i]における、C[i],B[i], A[i]の値を持つ
    A = {}
    B = {}
    C = {}
    ans_target = []
    ans_target.append(case[0][0])

    # Bを要所要所で復元する
    pos = 0
    pos_list = []
    bef_b = 0
    bef_a = 0
    for x, y in case:
        pos += y
        C[pos] = x
        B[pos] = x*y+bef_b
        A[pos] = y*(y+1)*C[pos]//2+bef_b*y+bef_a
        pos_list.append(pos)
        bef_a = A[pos]
        ans_target.append(A[pos])
        bef_b = B[pos]

    # print(pos == m)

    # Bが0になるポイントを探る
    for pre_i in range(len(pos_list)-1):
        cur_i = pre_i+1
        pre_pos = pos_list[pre_i]
        cur_pos = pos_list[cur_i]
        # Bの符号が、プラスからマイナスになったタイミングがチャンス
        if B[pre_pos] >= 0 and B[cur_pos] <= 0:
            c = C[cur_pos]
            # cはマイナスのはず
            if not (c <= 0):
                raise
            if c == 0:  # 自明に、Bは定数
                ans_target.append(A[cur_pos])
                continue
            add_pos = B[pre_pos]//(-c)
            bef_b = B[pre_pos]
            a = A[pre_pos] + add_pos*(add_pos+1)*c//2 + bef_b*add_pos
            ans_target.append(a)
            add_pos += 1
            if pre_pos + add_pos <= cur_pos:
                a = A[pre_pos] + add_pos*(add_pos+1)*c//2 + bef_b*add_pos
                ans_target.append(a)
    ans = max(ans_target)
    return ans


main()

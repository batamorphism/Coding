# 1点～10点（D点)の問題がp_i(<=100)個ある
# コンプリートボーナスの取り方別に、bit全探索する
# コンプリートボーナスを取ることを決めた問題は全部解いて、
# それ以外は、得点が高いものから貪欲に解いていく


def main():
    d, g = map(int, input().split())
    g //= 100
    pc_list = [tuple(map(int, input().split())) for _ in range(d)]
    pc_list = [(p, c//100) for p, c in pc_list]

    ans = float('inf')
    # コンプリートボーナスを取る問題を調べる
    ALL = 1 << d
    for bit in range(ALL):
        # print(bin(bit))
        c_list = [0]*d
        score = 0
        cnt = 0
        for c_ind in range(d):
            if (bit >> c_ind) & 1:
                c_list[c_ind] = 1
                score += pc_list[c_ind][1]
                score += pc_list[c_ind][0]*(c_ind+1)
                cnt += pc_list[c_ind][0]
        for c_ind in range(d-1, -1, -1):
            # 大きい問題から順に見ていく
            if c_list[c_ind]:  # 既に全部解いている
                continue
            if score >= g:
                break
            get_score = pc_list[c_ind][0]*(c_ind+1)  # 取得しうるスコア
            get_score = min(g - score, get_score)  # 不要な分は削る
            get_cnt = -(-get_score // (c_ind+1))  # 取得する問題数は切り上げ
            cnt += get_cnt
            score += get_score
        ans = min(ans, cnt)

    print(ans)


main()

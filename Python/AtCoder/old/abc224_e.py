import sys


def main():
    s = sys.stdin.readlines()
    r_end, c_end, n = map(int, s[0].split())
    # 各r, cに対して、その頂点含めて何回移動できるか
    DP_R = [0]*c_end  # 各列cに対して、行に対する最大値
    DP_C = [0]*r_end
    # DP = [[0]*c_end for _ in range(r_end)]  これはデカすぎ
    DP = {}  # 辞書型でもって高速化
    node_list = []
    s = s[1:]
    for ss in s:
        r, c, a = map(int, ss.split())
        r -= 1
        c -= 1
        node_list.append((a, r, c))
    node_list_original = node_list[:]
    node_list.sort(reverse=True)  # でっかい奴から埋めていけばよい

    pre_a = -1
    batch = {}
    for node in node_list:
        a, r, c = node
        if a != pre_a:
            # 違う数字が出てきたタイミングで、DPを反映
            for key, val in batch.items():
                rr, cc = key
                DP_R[cc] = max(val, DP_R[cc])
                DP_C[rr] = max(val, DP_C[rr])
            batch = {}
        dp = 0
        dp = DP_R[c]+1
        dp = max(DP_C[r]+1, dp)
        batch[(r, c)] = dp
        # DP_R[c] = dp
        # DP_C[r] = dp
        DP[(r, c)] = dp
        pre_a = a

    for node in node_list_original:
        a, r, c = node
        print(DP[(r, c)]-1)


main()

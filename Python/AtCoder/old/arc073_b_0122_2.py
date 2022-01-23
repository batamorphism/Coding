# 重さは高々4通り
def main():
    n, w = map(int, input().split())
    item_list = [tuple(map(int, input().split())) for _ in range(n)]
    w_0 = item_list[0][0]
    item_list = [(w_i-w_0, v_i) for w_i, v_i in item_list]

    # wは0, 1, 2, 3のいずれか
    values_of = [[] for _ in range(4)]
    for w_i, v_i in item_list:
        values_of[w_i].append(v_i)
    for values in values_of:
        values.sort(reverse=True)

    # 累積和
    for values in values_of:
        for i in range(1, len(values)):
            values[i] += values[i-1]

    # 0, 1, 2, 3それぞれをいくつ選ぶか
    ans = 0
    for w_is_0 in range(n+1):
        if w_is_0*w_0 > w:
            break
        for w_is_1 in range(n+1):
            if w_is_0*w_0 + w_is_1*(w_0+1) > w:
                break
            if w_is_0 + w_is_1 > n:
                break
            for w_is_2 in range(n+1):
                if w_is_0*w_0 + w_is_1*(w_0+1) + w_is_2*(w_0+2) > w:
                    break
                if w_is_0 + w_is_1 + w_is_2 > n:
                    break
                for w_is_3 in range(n+1):
                    if w_is_0*w_0 + w_is_1*(w_0+1) + w_is_2*(w_0+2) + w_is_3*(w_0+3) > w:
                        break
                    if w_is_0 + w_is_1 + w_is_2 + w_is_3 > n:
                        break
                    val = 0
                    for i, w_cnt in enumerate((w_is_0, w_is_1, w_is_2, w_is_3)):
                        if w_cnt <= len(values_of[i]) and w_cnt > 0:
                            val += values_of[i][w_cnt-1]
                    ans = max(ans, val)
    print(ans)


main()

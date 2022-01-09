# grundy
# b += w　して、 w -= 1　する
# b -= k ( 1 <= k <= b // 2)する
# 0 <= W, B <= 50
# したがって
# 0 <= w <= 50
# 0 <= b <= 50+49+...+1 = (51) * 50 // 2

# 敗北条件は
# w == 0 かつ b <= 1

def main():
    w_end = 50 + 1
    b_end = 51 * 50 // 2 + 1

    INF = float('inf')

    # grundy[w][b]
    grundy = [[-1] * b_end for _ in range(w_end)]
    grundy[0][0] = 0
    grundy[0][1] = 0

    for w in range(w_end):
        for b in range(b_end):
            nex_set = set()
            # 操作1
            nex_b = b + w
            nex_w = w - 1
            if nex_b < b_end and nex_w >= 0:
                nex_set.add(grundy[nex_w][nex_b])

            # 操作2
            nex_w = w
            for k in range(1, b // 2 + 1):
                nex_b = b - k
                if nex_b >= 0:
                    nex_set.add(grundy[nex_w][nex_b])

            for mex in range(len(nex_set)+1):
                if mex not in nex_set:
                    grundy[w][b] = mex
                    break

    n = int(input())
    W = list(map(int, input().split()))
    B = list(map(int, input().split()))
    grundy_list = []
    for w, b in zip(W, B):
        grundy_list.append(grundy[w][b])

    total_grundy = 0
    for g in grundy_list:
        total_grundy ^= g

    if total_grundy == 0:
        print('Second')
    else:
        print('First')


main()

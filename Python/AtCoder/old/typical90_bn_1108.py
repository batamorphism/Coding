# 末尾にxが足されると
# SUM(min(Ri-x, Ri-Li)/(Ri-Li+1))個だけ転倒数が増える
# 1-2, 1-2 の場合、
# 各末尾(100)に対し、各x(100)について、毎回min(Ri-x, Ri-Li)を計算(100)する

def main():
    n = int(input())
    LR_list = [tuple(map(int, input().split())) for _ in range(n)]

    ans = 0
    for x_ind, (le_x, ri_x) in enumerate(LR_list):
        prob = 1/(ri_x-le_x+1)
        for x in range(le_x, ri_x+1):
            sum_x = 0
            for le_i, ri_i in LR_list[:x_ind]:
                lo = max(le_i-1, x)
                lo = min(ri_i, lo)
                sum_x += (ri_i - lo)/(ri_i - le_i + 1)
            # print(x_ind, le_x, ri_x, sum_x, prob)
            ans += prob*sum_x
    print(ans)
    return


main()

def main():
    n, k = map(int, input().split())
    # cnt_of[a][b]で身長a, 体重bの人数
    # 1-ordered
    end_k = 5001
    cnt_of = [[0]*(end_k) for _ in range(end_k)]
    for _ in range(n):
        a, b = map(int, input().split())
        cnt_of[a][b] += 1

    # sum_of[a1][b1] = a<=a1, b<=b1の総和
    sum_of = [[0]*(end_k) for _ in range(end_k)]
    for a in range(end_k):
        for b in range(end_k):
            if a == 0 or b == 0:
                sum_of[a][b] = 0
                continue
            sum_of[a][b] = cnt_of[a][b]+sum_of[a][b-1]+sum_of[a-1][b]-sum_of[a-1][b-1]

    # calc_max_sum
    ans = 0
    for a0 in range(end_k):
        a1 = a0+k+1
        if a1 >= end_k:
            continue
        for b0 in range(end_k):
            b1 = b0+k+1
            if b1 >= end_k:
                continue
            ans = max(get_sum(a0, b0, a1, b1, sum_of), ans)

    print(ans)


def get_sum(a0, b0, a1, b1, sum_of):
    return sum_of[a1][b1]-sum_of[a1][b0]-sum_of[a0][b1]+sum_of[a0][b0]


main()

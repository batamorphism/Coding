def main():
    # 累積和
    n = int(input())
    score1_of = [0] * (n + 1)
    score2_of = [0] * (n + 1)

    for i in range(n):
        c, p = map(int, input().split())
        if c == 1:
            score1_of[i] = p
        else:
            score2_of[i] = p

    data1 = [0] * (n + 10)
    data2 = [0] * (n + 10)

    def get_sum(data, le, ri):
        # [le, ri]の累積和を与える
        le += 1
        ri += 1
        return data[ri] - data[le-1]

    for i, val in enumerate(score1_of):
        pos = i + 1
        data1[pos] = data1[pos-1] + val

    for i, val in enumerate(score2_of):
        pos = i + 1
        data2[pos] = data2[pos-1] + val

    q = int(input())
    for _ in range(q):
        le, ri = map(int, input().split())
        le -= 1
        ri -= 1
        print(get_sum(data1, le, ri), get_sum(data2, le, ri))


main()

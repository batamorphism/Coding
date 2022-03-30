def main():
    n = int(input())
    A = list(map(int, input().split()))
    degree_list = [0]
    degree = 0
    for a in A:
        degree += a
        degree %= 360
        degree_list.append(degree)

    degree_list.sort()
    degree_list.append(360)
    ans = -1
    for i, d_i in enumerate(degree_list[:-1]):
        nex_d = degree_list[i + 1]
        pre_ans = nex_d - d_i
        ans = max(ans, pre_ans)
    print(ans)


main()

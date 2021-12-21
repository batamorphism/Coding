def main():
    n = int(input())
    AB = [list(map(int, input().split())) for _ in range(n)]

    # *123420
    #  1111-2-2
    i_end = 10**6+10
    imos = [0]*i_end
    for le, ri in AB:
        # leで+1, ri+1で-1
        imos[le] += 1
        imos[ri+1] -= 1

    cnt = 0
    max_cnt = 0
    for delta in imos:
        cnt += delta
        if cnt > max_cnt:
            max_cnt = cnt

    print(max_cnt)


main()

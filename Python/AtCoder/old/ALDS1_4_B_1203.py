def main():
    _ = int(input())
    S = list(map(int, input().split()))
    _ = int(input())
    T = list(map(int, input().split()))

    # Sを座標圧縮
    tmp = sorted(list(set(S)))
    S_zipper = {a: i for i, a in enumerate(tmp)}
    del tmp
    S_zip = [S_zipper[s] for s in S]

    s_cnt = [0]*len(S_zipper)
    for s in S_zip:
        s_cnt[s] += 1

    ans = 0
    for t in T:
        if t in S_zipper:
            ans += 1

    print(ans)


main()

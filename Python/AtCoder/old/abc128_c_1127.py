# bit全探索
def main():
    N, M = map(int, input().split())

    query_list = []
    for _ in range(M):
        k, *S = map(int, input().split())
        S = [s-1 for s in S]
        query_list.append(S)
    P = list(map(int, input().split()))
    # スイッチの付き方を全部試す
    ALL_n = 1 << N
    n_list = [0] * N
    ans = 0
    for bit_n in range(ALL_n):
        for n in range(N):
            if bit_n >> n & 1:
                n_list[n] = 1
            else:
                n_list[n] = 0
        is_ok = True  # 全てのスイッチがONである
        for p, S in zip(P, query_list):
            cnt = 0
            for s in S:
                cnt += n_list[s]
            if cnt % 2 != p:
                is_ok = False
                break
        if is_ok:
            ans += 1

    print(ans)


main()

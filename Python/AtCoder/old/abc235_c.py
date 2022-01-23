def main():
    n, q = map(int, input().split())
    A = list(map(int, input().split()))

    # aを座標圧縮
    zip_A = {a: i for i, a in enumerate(sorted(list(set(A))))}
    A = [zip_A[a] for a in A]
    # d[a] = aが出てきた場所からなるリスト
    d = [[] for _ in range(n+1)]
    for i, a in enumerate(A):
        d[a].append(i)

    ans_list = []
    for _ in range(q):
        x, k = map(int, input().split())
        k -= 1
        if x not in zip_A:
            ans_list.append(-1)
            continue
        else:
            x = zip_A[x]
            d_x = d[x]
            if len(d_x) <= k:
                ans_list.append(-1)
                continue
            ans = d_x[k]
            ans_list.append(ans+1)

    print(*ans_list, sep='\n')


main()

def main():
    n, q = map(int, input().split())
    MOD = 10**9 + 7
    query = []
    for _ in range(q):
        x, y, z, w = map(int, input().split())
        x -= 1
        y -= 1
        z -= 1
        query.append((x, y, z, w))

    # Aの下からi bit目を見る
    ans = 1
    for i in range(60):
        ans_i = 0
        query_i = []
        for x, y, z, w in query:
            w = (w >> i) & 1
            query_i.append((x, y, z, w))
        # aのi bit目を0とするか1とするかを全探索
        for bit in range(1 << n):
            is_ok = True  # このbitの選び方がqueryと適合するか
            for x, y, z, w in query_i:
                x_bit = (bit >> x) & 1
                y_bit = (bit >> y) & 1
                z_bit = (bit >> z) & 1
                if (x_bit | y_bit | z_bit) != w:
                    is_ok = False
                    break
            if is_ok:
                ans_i += 1
        ans *= ans_i
        ans %= MOD

    print(ans)


main()

mod = 10**9+7


def main():
    n, q = map(int, input().split())
    query_list = []
    for _ in range(q):
        x, y, z, w = map(int, input().split())
        x -= 1
        y -= 1
        z -= 1
        query_list.append((x, y, z, w))

    # 各bitに対し独立に考える
    # 各bit毎に、条件を満たす組み合わせ数を求める
    ALL = 1 << n
    A = [0]*n
    ans = 1
    for num in range(60):
        cnt = 0
        for bit in range(ALL):
            # 各A[i]がnumを持っているか
            for i in range(n):
                if bit >> i & 1:
                    A[i] = 1
                else:
                    A[i] = 0
            is_ok = True
            for query in query_list:
                x, y, z, w = query
                # A[x] or A[y] or A[z] がwとなるか
                if w >> num & 1:
                    if not(A[x] or A[y] or A[z]):
                        is_ok = False
                        break
                else:
                    if A[x] or A[y] or A[z]:
                        is_ok = False
                        break
            if is_ok:
                cnt += 1
        ans *= cnt
        ans %= mod

    print(ans)


main()

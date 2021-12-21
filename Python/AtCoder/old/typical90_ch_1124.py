# bit毎に独立に考える
# 0<= a_i < 1<<60 なので、60桁考えればよい
mod = 10**9+7
dig_end = 60
# a_x or a_y or a_z = w
# 各a_iについて、0, 1を全探索
# 条件を満たした数をcntとし、cntのproductが答え


def main():
    n, q = map(int, input().split())
    query_list = []
    for _ in range(q):
        x, y, z, w = map(int, input().split())
        x, y, z = x-1, y-1, z-1
        query_list.append((x, y, z, w))
    prod_list = []
    bit_end = n
    all = 1 << bit_end

    for dig in range(dig_end):
        cnt = 0
        for bit in range(all):
            # A[i]のdig桁目のbitが0か1か
            a_bit = []
            for a_i in range(bit_end):
                if (bit >> a_i) & 1:
                    a_bit.append(1)
                else:
                    a_bit.append(0)
            is_ok = True
            for x, y, z, w in query_list:
                w_bit = (w >> dig) & 1
                if a_bit[x] | a_bit[y] | a_bit[z] != w_bit:
                    is_ok = False
                    break
            if is_ok:
                cnt += 1
        prod_list.append(cnt)

    ans = 1
    for p in prod_list:
        ans *= p
        ans %= mod
    print(ans)


main()

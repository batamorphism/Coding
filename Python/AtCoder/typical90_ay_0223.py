# 半分全列挙
# 左からcnt_le個選んだ場合に、考えうる値段のリストを作成する
from collections import defaultdict


def main():
    n, cnt_target, price_max = map(int, input().split())
    A = list(map(int, input().split()))
    mid = n//2
    A_le = A[:mid]
    A_ri = A[mid:]

    le_price_list_of = defaultdict(list)
    ri_price_list_of = defaultdict(list)

    def calc_price_list_of(A, price_list_of):
        ALL = 1 << len(A)
        for bit in range(ALL):
            cnt = popcount(bit)
            price = 0
            for i, a_i in enumerate(A):
                if bit >> i & 1:
                    price += a_i
            price_list_of[cnt].append(price)
        for price_list in price_list_of.values():
            price_list.sort()

    calc_price_list_of(A_le, le_price_list_of)
    calc_price_list_of(A_ri, ri_price_list_of)

    ans = 0
    for cnt_le, le_price_list in le_price_list_of.items():
        cnt_ri = cnt_target - cnt_le
        if cnt_ri < 0:
            continue
        ri_price_list = ri_price_list_of[cnt_ri]
        for le_price in le_price_list:
            ri_price_max = price_max - le_price
            if ri_price_max < 0:
                continue
            # ri_price_max以下の要素数がri_price_listにいくつあるか
            ok = -1
            ng = len(ri_price_list)
            while ng - ok > 1:
                mid = (ok + ng) // 2
                if ri_price_list[mid] <= ri_price_max:
                    ok = mid
                else:
                    ng = mid
            ans += ok + 1
    print(ans)


def popcount(S):
    return bin(S).count('1')


main()

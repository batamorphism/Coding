# 半分全列挙

def main():
    n, k, p = map(int, input().split())
    A = list(map(int, input().split()))
    A1 = A[:n//2]
    A2 = A[n//2:]

    # price_of_list[個数][ind] = 金額
    price_of_list1 = [[] for _ in range(n+1)]
    price_of_list2 = [[] for _ in range(n+1)]
    set_price_of_list(A1, price_of_list1)
    set_price_of_list(A2, price_of_list2)

    ans = 0
    for k1 in range(len(A1)+1):
        k2 = k - k1
        if k2 < 0:
            continue
        price_list1 = price_of_list1[k1]
        price_list2 = price_of_list2[k2]
        for price1 in price_list1:
            # price1 + price2 <= p
            # price2 <= p - price1
            price2_max = p - price1
            if price2_max < 0:
                continue
            ok = -1
            ng = len(price_list2)
            while ng - ok > 1:
                mid = (ok + ng) // 2
                if price_list2[mid] <= price2_max:
                    ok = mid
                else:
                    ng = mid
            ans += ok + 1

    print(ans)


def set_price_of_list(A, price_of_list):
    n = len(A)
    ALL = 1 << n
    for bit in range(ALL):
        cnt = 0
        price = 0
        for i, a_i in enumerate(A):
            if bit & (1 << i):
                cnt += 1
                price += a_i
        price_of_list[cnt].append(price)
    for price_list in price_of_list:
        price_list.sort()


main()

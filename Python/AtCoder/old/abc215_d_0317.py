# エラトステネスの篩
# Aの素因数を全て求める
# 全ての素因数で割り切れない数を列挙する
def main():
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    a_max = max(A)
    a_max = max(a_max, m, 100)

    is_prime = [True] * (a_max+1)
    div_of = [val for val in range(a_max+1)]
    is_prime[0] = False
    is_prime[1] = False
    for val in range(2, a_max+1):
        if is_prime[val]:
            for val2 in range(val**2, a_max+1, val):
                is_prime[val2] = False
                div_of[val2] = val

    # Aの素因数全体
    div_set = set()
    for a_i in A:
        while a_i != 1:
            div = div_of[a_i]
            div_set.add(div)
            a_i //= div

    ans_list = []
    # print(div_set)
    for k in range(1, m+1):
        is_ans = True
        for div in div_set:
            if k % div == 0 and div != 1:
                is_ans = False
                break
        if is_ans:
            ans_list.append(k)
    ans_list.sort()
    print(len(ans_list))
    print(*ans_list)


main()

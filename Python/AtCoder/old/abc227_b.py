def main():
    n = int(input())
    S_list = list(map(int, input().split()))

    # Sのうち、4ab+3a+3bの形にならない物を探す
    # 各a, bはそれぞれ400以下であり、400**2 = 160000パターンしかない
    true_set = set()
    for a in range(1, 401):
        for b in range(1, 401):
            val = 4*a*b + 3*a + 3*b
            true_set.add(val)

    cnt = 0
    for s in S_list:
        if s not in true_set:
            cnt += 1

    print(cnt)


main()

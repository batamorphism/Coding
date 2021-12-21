def main():
    n, m = map(int, input().split())
    pair_list = [list(map(int, input().split())) for _ in range(m)]

    # n <= 12
    # n人がそれぞれ派閥に入るかを全パターン試す
    # 考えうるパターンは2**n
    ans = 0

    for i in range(1 << n):
        group = []
        for human in range(n):
            if (i >> human & 1):
                group.append(human+1)

        makable = True
        for human_1 in group:
            for human_2 in group:
                if human_2 >= human_1:
                    break
                # human2<human1
                if [human_2, human_1] not in pair_list:
                    makable = False
        if makable:
            ans = max(len(group), ans)

    print(ans)


main()

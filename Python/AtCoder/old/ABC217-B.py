def main():
    S = []
    for _ in range(3):
        s = input()
        S.append(s)
    contests = ['ABC', 'ARC', 'AGC', 'AHC']

    for c in contests:
        flag = False
        for s in S:
            if s == c:
                flag = True
        if not flag:  # コンテストcは開催されていない
            print(c)


main()

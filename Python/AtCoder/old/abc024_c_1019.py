def main():
    n, d, k = map(int, input().split())
    LR = [tuple(map(int, input().split())) for _ in range(d)]
    ST = [tuple(map(int, input().split())) for _ in range(k)]

    for st in ST:
        s, t = st
        cur = s
        for i, lr in enumerate(LR):
            l, r = lr
            if l <= cur <= r:
                if l <= t <= r:
                    # goal
                    print(i+1)
                    break
                if t >= cur:
                    cur = r
                else:
                    cur = l


main()

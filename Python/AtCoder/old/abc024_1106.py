def main():
    n, d, k = map(int, input().split())
    Days = [tuple(map(int, input().split())) for _ in range(d)]
    Peoples = [tuple(map(int, input().split())) for _ in range(k)]

    for st, en in Peoples:
        # stからenへ移動を開始する
        move(st, en, Days)


def move(st, en, Days):
    cur = st
    for day, lr in enumerate(Days):
        le, ri = lr
        if le <= cur <= ri:
            # 移動する
            if en > cur:
                cur = min(ri, en)  # 右に移動
            else:
                cur = max(le, en)  # 左に移動
        if cur == en:
            # 移動が終了した
            print(day + 1)
            return


main()

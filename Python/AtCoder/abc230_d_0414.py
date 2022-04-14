# 区間スケジューリング
def main():
    n, d = map(int, input().split())
    punched = -float('inf')  # 一番最後にパンチした場所
    # punched+d-1まで破壊される
    item_list = []
    for _ in range(n):
        le, ri = map(int, input().split())
        item_list.append((le, ri))
    item_list.sort(key=lambda x: x[1])
    # 締め切りが近い順に見る
    ans = 0
    for le, ri in item_list:
        if le > punched+d-1:
            # こいつはまだ破壊されていない
            punched = ri
            ans += 1
    print(ans)


main()

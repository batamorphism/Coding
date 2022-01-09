# 区間スケ
def main():
    node_end, item_end = map(int, input().split())
    node_end -= 1
    item_list = []
    for _ in range(item_end):
        le, ri = map(int, input().split())
        le -= 1
        ri -= 1
        # [le, ri]を通れないようにするためには
        # le, ..., ri-1番目の橋のいずれかが破壊されていればよい
        ri -= 1
        item_list.append((le, ri))

    item_list.sort(key=lambda x: x[1])

    # 区間スケジューリング
    INF = float('inf')
    cnt = 0
    destroy = -INF
    for le, ri in item_list:
        if le > destroy:
            cnt += 1
            destroy = ri

    print(cnt)


main()

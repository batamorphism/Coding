# 区間スケジューリング
# [a_i, b_i)の間のどこかで、少なくとも一回橋を壊せ
def main():
    n, m = map(int, input().split())
    item_list = []
    for _ in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        item_list.append((a, b-1))
    # bを-1した
    # これにより、[a, b]の間にあるいずれかの橋を破壊せよ、という問題になった

    item_list.sort(key=lambda x: x[1])

    ans = 0
    broken = -float('inf')
    for le, ri in item_list:
        # 今まで壊した橋の右端の位置が
        # leより小さい場合、riをbrokenとする
        if broken < le:
            broken = ri
            ans += 1

    print(ans)


main()

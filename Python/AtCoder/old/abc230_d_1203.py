# 区間スケジューリング
# le側をD-1だけ小さくしたスケジューリング問題だと思えばよい
# 簡単のために、ri側をD-1だけ大きくしたスケジューリング問題だと思うことにする

def main():
    n, d = map(int, input().split())
    item_list = []
    for _ in range(n):
        le, ri = map(int, input().split())
        le -= (d-1)
        item_list.append((le, ri))
    item_list.sort(key=lambda x: x[1])
    ri_bef = item_list[0][1]
    ans = 0
    # print(item_list)
    for le, ri in item_list:
        # 今まで見てきたriより、大きいleが出てきたらリセット
        if le > ri_bef:
            ri_bef = ri
            ans += 1
    print(ans+1)


main()

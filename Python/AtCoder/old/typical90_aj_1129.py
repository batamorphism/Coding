# マンハッタン距離は45度回転
#  1 1
# -1 1を乗算する
def main():
    n, q = map(int, input().split())
    point_list = []
    for _ in range(n):
        x, y = map(int, input().split())
        x, y = x+y, y-x
        point_list.append((x, y))

    query_list = [int(input())-1 for _ in range(q)]

    lo_x = min(point_list, key=lambda x: x[0])[0]
    hi_x = max(point_list, key=lambda x: x[0])[0]
    lo_y = min(point_list, key=lambda x: x[1])[1]
    hi_y = max(point_list, key=lambda x: x[1])[1]

    for query in query_list:
        x, y = point_list[query]
        ans = max(abs(lo_x-x), abs(hi_x-x), abs(lo_y-y), abs(hi_y-y))
        print(ans)


main()

# Lを反映し、頂点が重複するか
# Rを反映し、頂点が重複するか
def main():
    n = int(input())
    xy_list = [tuple(map(int, input().split())) for _ in range(n)]
    S = input()

    # 座標圧縮
    # 各yについて処理する
    x_list = []
    y_list = []
    for x, y in xy_list:
        x_list.append(x)
        y_list.append(y)

    x_zipper = {x: i for i, x in enumerate(sorted(set(x_list)))}
    y_zipper = {x: i for i, x in enumerate(sorted(set(y_list)))}
    xy_list = [(x_zipper[x], y_zipper[y]) for x, y in xy_list]
    x_list = [x_zipper[x] for x in x_list]
    y_list = [y_zipper[y] for y in y_list]
    max_y = max(y_list)

    L_list_of = [[] for _ in range(max_y + 1)]
    R_list_of = [[] for _ in range(max_y + 1)]

    for i in range(n):
        c = S[i]
        x, y = xy_list[i]
        if c == 'L':
            L_list_of[y].append(x)
        else:
            R_list_of[y].append(x)

    # 各yについて、Lのうち最小の者 <= Rのうち最大の者であれば衝突
    for y in range(max_y+1):
        L_list = L_list_of[y]
        R_list = R_list_of[y]
        if len(L_list) == 0 or len(R_list) == 0:
            continue
        l_min = max(L_list)
        r_max = min(R_list)
        if l_min >= r_max:
            print('Yes')
            return

    print('No')


main()

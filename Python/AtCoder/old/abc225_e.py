class Degree():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __lt__(self, other):
        # self < other
        # self.y/self.x < other.y/other.x
        # self.y*other.x < self.x*other.y
        return self.y*other.x < self.x*other.y

    def __le__(self, other):
        return self.y*other.x <= self.x*other.y


def main():
    n = int(input())
    p_list = []
    for _ in range(n):
        x, y = map(int, input().split())
        x1 = x-1
        y2 = y-1
        p_list.append((Degree(x1, y), Degree(x, y2)))  # xは必ず一致
    # 区間スケジューリング問題
    # 偏角はy1/x1->誤差をなくすためにクラス化
    p_list.sort()  # 上点の角度が浅い順にソート
    ans = 0
    max_degree = Degree(1, -1)
    for hi_degree, lo_degree in p_list:
        if max_degree <= lo_degree:
            ans += 1
            max_degree = hi_degree

    print(ans)


main()

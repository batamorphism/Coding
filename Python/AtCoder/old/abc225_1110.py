class Rational:
    def __init__(self, a, b):
        # 分子, 分母で宣言
        self.numerator = a
        self.denominator = b

    def __lt__(self, other):
        # self < other
        # 分子を比較
        return self.numerator * other.denominator < self.denominator * other.numerator


def main():
    n = int(input())
    degree_list = []
    for _ in range(n):
        x, y = map(int, input().split())
        x1, y1 = x-1, y
        x2, y2 = x, y-1
        degree_st = Rational(y2, x2)
        degree_en = Rational(y1, x1)
        # print(degree_st < degree_en)
        degree = (degree_en, degree_st)  # 終わるのが早い順にソートする
        degree_list.append(degree)

    degree_list.sort()

    # 区間スケジューリング
    ans = 0
    pre_en = Rational(-1, 1)
    for en, st in degree_list:
        if not st < pre_en:
            pre_en = en
            ans += 1

    print(ans)


main()

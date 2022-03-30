class Rational:
    def __init__(self, up, down):
        self.up = up
        self.down = down

    def __le__(self, other):
        # self < otherを定義
        # (a/b) <= (c/d)
        # a*d <= c*b
        return self.up * other.down <= other.up * self.down

    def __lt__(self, other):
        return self.up * other.down < other.up * self.down

    def __repr__(self):
        return str(self.up) + "/" + str(self.down)


def main():
    n = int(input())
    point_list = []
    for i in range(n):
        x, y = map(int, input().split())
        # 角度は、y/xで表される
        lo = Rational(y-1, x)
        hi = Rational(y, x-1)
        point_list.append((lo, hi, i))

    # 区間スケジューリング
    # hi側でソートして、貪欲に取っていく
    point_list.sort(key=lambda x: x[1])

    ans = 0
    cur_point = Rational(-1, 0)
    for lo, hi, i in point_list:
        if cur_point <= lo:
            # print(lo, i)
            ans += 1
            cur_point = hi

    print(ans)


main()

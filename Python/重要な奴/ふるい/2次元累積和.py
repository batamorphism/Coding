class cum_sum_2d:
    """
    2次元累積和
    List : = 累積和をとる対象の2次元リスト
    """
    def __init__(self, list_2d: list):
        """
        list_2d: 2次元累積和をとる対象の2次元リスト
        """
        h = len(list_2d)
        w = len(list_2d[0])

        # init_sum
        self.sum = [[0]*w for _ in range(h)]
        self.sum[0][0] = list_2d[0][0]
        for c in range(1, w):   # set first column
            self.sum[0][c] = self.sum[0][c-1] + list_2d[0][c]
        for r in range(1, h):   # set rows
            cnt_r = 0
            for c in range(w):
                cnt_r += list_2d[r][c]
                self.sum[r][c] = self.sum[r-1][c] + cnt_r

    def get_sum(self, r_0, c_0, r_1, c_1):
        """
        (r_0, c_0)と(r_1, c_1)に囲まれた領域の総和
        ここで、r_0, c_0は0から始まる
        すなわち、(r_0, c_0)=(r_1, c_1) = (0, 0)の場合
        リストの一番左上の1セルが出力される
        """
        if r_0 > r_1 or c_0 > c_1:
            return 0
        elif r_0 == 0 and c_0 == 0:
            return self.sum[r_1][c_1]
        elif r_0 == 0:
            return self.sum[r_1][c_1] - self.sum[r_1][c_0-1]
        elif c_0 == 0:
            return self.sum[r_1][c_1] - self.sum[r_0-1][c_1]
        else:
            return (self.sum[r_1][c_1]
                    - self.sum[r_1][c_0-1]
                    - self.sum[r_0-1][c_1]
                    + self.sum[r_0-1][c_0-1])


def main():
    h, w, *A = map(int, open(0).read().split())
    c = [[A[r*w+c] for c in range(w)] for r in range(h)]

    # c =1  2  3  4
    #    5  6  7  8
    #    9 10 11 12
    da = cum_sum_2d(c)
    print(da.get_sum(0, 0, 1, 1))  # 1+2+5+6 = 14
    print(da.get_sum(1, 1, 1, 1))  # 6 1は2行2列目を指すので、6が出力
    print(da.get_sum(1, 1, 2, 2))  # 6+7+10+11 = 34
    print(da.get_sum(0, 1, 1, 2))  # 2+3+6+7 = 18
    print(cum_sum_2d(c).get_sum(0, 1, 1, 2))


main()

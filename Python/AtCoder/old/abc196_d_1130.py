# 全探索
class RCCounter:
    def __init__(self, r_end, c_end):
        self._r_end = r_end
        self._c_end = c_end
        self.r = 0
        self.c = 0

    def next(self):
        self.c += 1
        if self.c == self._c_end:
            self.r += 1
            self.c = 0

    def back(self):
        self.c -= 1
        if self.c == -1:
            self.r -= 1
            self.c = self._c_end - 1

    def is_end(self):
        return self.r >= self._r_end


def main():
    r_end, c_end, a_max, b_max = map(int, input().split())
    it = RCCounter(r_end, c_end)
    grid = [[0] * c_end for _ in range(r_end)]

    ans = [0]

    def dfs(a, b):
        # print(it.r, it.c, a, b, it.is_end())
        if it.is_end():
            """
            print('---')
            for g in grid:
                print(g)
            """
            ans[0] += 1
            return
        if grid[it.r][it.c] != 0:
            # ここにはもう畳を敷く必要がないから、次へ
            it.next()
            dfs(a, b)
            it.back()
            return
        for ori in range(3):
            # 0だったら、1*1の畳を敷く
            # 1だったら、1*2の畳を敷く
            # 2だったら、2*1の畳を敷く
            if ori == 0:
                if b > 0:
                    grid[it.r][it.c] = 1+ori
                    b -= 1
                else:
                    continue
            if ori == 1:
                if it.c + 1 >= c_end or a <= 0:
                    continue
                if grid[it.r][it.c+1] != 0:
                    continue
                grid[it.r][it.c] = 1+ori
                grid[it.r][it.c+1] = 1+ori
                a -= 1
            if ori == 2:
                if it.r + 1 >= r_end or a <= 0:
                    continue
                if grid[it.r+1][it.c] != 0:
                    continue
                grid[it.r][it.c] = 1+ori
                grid[it.r+1][it.c] = 1+ori
                a -= 1
            it.next()
            dfs(a, b)
            it.back()
            # 帰りがけに、元に戻す
            if ori == 0:
                b += 1
            else:
                a += 1
            grid[it.r][it.c] = 0
            if ori == 1:
                grid[it.r][it.c+1] = 0
            if ori == 2:
                grid[it.r+1][it.c] = 0

    dfs(a_max, b_max)
    print(ans[0])


main()

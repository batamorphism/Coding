class BIT:
    def __init__(self, n, MOD=None):
        self.bit_end = n + 10
        self.bit_dat = [0] * self.bit_end
        self.bit_all = 0
        self.MOD = MOD

    def add(self, pos, val):
        pos += 1
        while pos < self.bit_end:
            self.bit_dat[pos] += val
            if self.MOD:
                self.bit_dat[pos] %= self.MOD
            pos += pos & -pos
        self.bit_all += val
        if self.MOD:
            self.bit_all %= self.MOD

    def get_sum(self, pos):
        # [0, ...., pos]の総和を取る
        pos += 1
        ret = 0
        while pos > 0:
            ret += self.bit_dat[pos]
            pos -= pos & -pos
        if self.MOD:
            ret %= self.MOD
        return ret

    def get_one_val(self, pos):
        # [pos]の値を取る
        ret = self.get_sum(pos) - self.get_sum(pos - 1)
        if self.MOD:
            ret %= self.MOD
        return ret

    def get_leq(self, pos):
        # [0, ..., pos]の総和を取る
        ret = self.get_sum(pos)
        if self.MOD:
            ret %= self.MOD
        return ret

    def get_geq(self, pos):
        # [pos, ...]の総和を取る
        ret = self.bit_all - self.get_sum(pos - 1)
        if self.MOD:
            ret %= self.MOD
        return ret

    def get_lt(self, pos):
        # [0, ..., pos)の総和を取る
        ret = self.get_sum(pos-1)
        if self.MOD:
            ret %= self.MOD
        return ret

    def get_gt(self, pos):
        # (pos, ...]の総和を取る
        ret = self.bit_all - self.get_sum(pos)
        if self.MOD:
            ret %= self.MOD
        return ret

    def debug(self):
        # 全ての値を出力する
        for i in range(self.bit_end):
            print(i, self.bit_dat[i])

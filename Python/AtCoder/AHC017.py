def main():
    dr_dc = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    cur_node = (0, 0)
    for dr, dc in dr_dc:
        nex_node = (cur_node[0] + dr, cur_node[1] + dc)
        # Python
        # mutable   : 変更可能。参照になる。ハッシュの計算ができない。
        # immutable : 変更不能。値になる。ハッシュの計算ができる。
    # string: immutable
    a = "abc"
    b = a  # bへaのコピーが発生する。
    a = "longtextlongtextlongtextlongtextlongtextlongtextlongtextlongtextlongtext"
    for _ in range(100):
        b = a  # めっちゃ遅い
        if b in trase:
            pass
    # list: mutable
    # tuple: immutable
    # list [0, 1, 2]
    # tuple (0, 1, 2)

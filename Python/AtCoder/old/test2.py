# seg_tree

def update(pos, val):
    global seg_tree
    seg_tree[pos] = val
    while pos > 0:
        pos = (pos - 1) // 2
        seg_tree[pos] = seg_tree[pos * 2 + 1] + seg_tree[pos * 2 + 2]

def query(le, ri):
    global seg_tree
    res = 0
    while le < ri:
        if le % 2 == 1:
            res += seg_tree[le]
            le += 1
        if ri % 2 == 0:
            ri -= 1
            res += seg_tree[ri]
        le = (le + 1) // 2
        ri = (ri - 1) // 2
    return res
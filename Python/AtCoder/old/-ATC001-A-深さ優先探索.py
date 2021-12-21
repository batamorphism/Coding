"""
高橋君の住む街は長方形の形をしており、格子状の区画に区切られています。
長方形の各辺は東西及び南北に並行です。
各区画は道または塀のどちらかであり、
高橋君は道を東西南北に移動できますが斜めには移動できません。 
また、塀の区画は通ることができません。

高橋君が、塀を壊したりすることなく
道を通って魚屋にたどり着けるかどうか判定してください。
"""
import sys

# 再帰できる上限を引き上げる
sys.setrecursionlimit(200000)


def main():
    ip = open(0).read().split()

    st = State()
    h, w = map(int, ip[:2])
    c0 = list(ip[2:])
    c = [list(c0[i]) for i in range(h)]

    st.h = h
    st.w = w
    st.c = c

    for i in range(h):
        for j in range(w):
            if st.c[i][j] == 's':
                sy, sx = i, j  # スタート位置

    dfs(sy, sx, st)
    if not st.is_finished:
        print('No')


def dfs(y, x, st):
    # 探索中の枝が条件を満たさない場合は、何もせず一個戻る
    if not check(y, x, st):
        return
    # 停止条件
    if st.c[y][x] == 'g':
        print('Yes')
        st.is_finished = True
    #pre_c = copy.deepcopy(st.c)
    st.c[y][x] = '*'
    #print(*st.c, sep='\n')
    #print('----------')
    dfs(y+1, x, st)
    dfs(y-1, x, st)
    dfs(y, x+1, st)
    dfs(y, x-1, st)

    # 問題によっては、次の1ステップ戻る処理を入れる
    #st.c[y][x] = '.'


def check(y, x, st):
    # 壁に当たったり、探索範囲外になった場合はダメ
    if not(0 <= y < st.h) or not(0 <= x < st.w): 
        return False
    elif st.c[y][x] == "#" or st.c[y][x] == "*":
        return False
    else:
        return True


class State:
    def __init__(self):
        self.h = 0
        self.w = 0
        self.c = []
        self.is_finished = False


main()

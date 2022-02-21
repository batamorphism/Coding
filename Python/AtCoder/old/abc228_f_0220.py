import copy
from collections import deque
import heapq as hp


# 高橋君のスコアは、taka_h, taka_wの矩形領域の総和
# 青木君のスコアは、aoki_h, aoki_wの矩形領域の総和
# 高橋君がr, cにスタンプを打った場合
# 青木君は、h, wの領域のスライド最大値を取り
# そのスコアが減算される
# スライドする幅は、taka_h-aoki_h, taka_w-aoki_wとなる
def main():
    r_end, c_end, taka_h, taka_w, aoki_h, aoki_w = map(int, input().split())
    aoki_h = min(aoki_h, taka_h)
    aoki_w = min(aoki_w, taka_w)

    # 累積和は1-indexed
    r_end, c_end = r_end+1, c_end+1
    grid = [[0]*c_end for _ in range(r_end)]
    for r in range(1, r_end):
        row = list(map(int, input().split()))
        for c in range(1, c_end):
            grid[r][c] = row[c-1]

    # 高橋君が獲得するスコアは、
    # taka_h, taka_wの矩形領域の総和
    # しゃくとり法
    Taka_score = copy.deepcopy(grid)
    for r in reversed(range(1, r_end)):
        que = deque()
        sum_ = 0
        for c in reversed(range(1, c_end)):
            val = Taka_score[r][c]
            sum_ += val
            que.appendleft(val)
            while que and not len(que) <= taka_w:
                rm = que.pop()
                sum_ -= rm
            Taka_score[r][c] = sum_
    for c in reversed(range(1, c_end)):
        que = deque()
        sum_ = 0
        for r in reversed(range(1, r_end)):
            val = Taka_score[r][c]
            sum_ += val
            que.appendleft(val)
            while que and not len(que) <= taka_h:
                rm = que.pop()
                sum_ -= rm
            Taka_score[r][c] = sum_

    """
    for s in Taka_score:
        print(s)
    """

    # 青木君が獲得するスコアは、
    # aoki_h, aoki_wの矩形領域の総和
    # しゃくとり法
    Aoki_score = copy.deepcopy(grid)
    for r in reversed(range(1, r_end)):
        que = deque()
        sum_ = 0
        for c in reversed(range(1, c_end)):
            val = Aoki_score[r][c]
            sum_ += val
            que.appendleft(val)
            while que and not len(que) <= aoki_w:
                rm = que.pop()
                sum_ -= rm
            Aoki_score[r][c] = sum_
    for c in reversed(range(1, c_end)):
        que = deque()
        sum_ = 0
        for r in reversed(range(1, r_end)):
            val = Aoki_score[r][c]
            sum_ += val
            que.appendleft(val)
            while que and not len(que) <= aoki_h:
                rm = que.pop()
                sum_ -= rm
            Aoki_score[r][c] = sum_

    # 高橋君がr, cに打った時
    # 青木君は、(r, c)~(r+slide_h, c+slide_w)のうち最大値のスコアを採用する
    # スライド最大値
    slide_h = taka_h - aoki_h
    slide_w = taka_w - aoki_w
    for r in reversed(range(1, r_end)):
        que = []
        for c in reversed(range(1, c_end)):
            val = Aoki_score[r][c]
            hp.heappush(que, (-val, c))
            while que[0][1] > c+slide_w:
                hp.heappop(que)
            Aoki_score[r][c] = -que[0][0]
    for c in reversed(range(1, c_end)):
        que = []
        for r in reversed(range(1, r_end)):
            val = Aoki_score[r][c]
            hp.heappush(que, (-val, r))
            while que[0][1] > r+slide_h:
                hp.heappop(que)
            Aoki_score[r][c] = -que[0][0]

    ans = -float('inf')
    for r in range(r_end):
        for c in range(c_end):
            score = Taka_score[r][c] - Aoki_score[r][c]
            ans = max(ans, score)
    print(ans)


main()

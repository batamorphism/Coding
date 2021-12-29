import heapq as hp
import random
import matplotlib.pyplot as plt


def main():
    base_rate = 2.5  # 復習間隔の伸び率
    easy_bonus = 1.3  # 簡単と回答した時のボーナス
    wrong_penalty = 0.2  # 間違えた時のペナルティ よくわからない・・・
    collect_rate = 0.96  # 正答率
    collect_rate_first = 0.5  # 最初の正答率
    dur_norm = 7  # 復習開始までの間隔
    dur_easy = 30  # 簡単の場合の間隔
    day_last = 356  # 何日間やるか
    num_per_day = 2  # 一日何問解くか

    que = []
    ans = 0
    # 初日
    day = 0

    for day in range(day_last):
        for _ in range(num_per_day):
            if que and que[0][0] <= day:
                # 期日を過ぎている場合は、復習開始
                pre_day, pre_dur, pre_rate = hp.heappop(que)
                if random.random() >= collect_rate:
                    # 不正解だった場合
                    cur_day = day + 1  # 翌日にやる
                    cur_dur = dur_norm
                    cur_rate = pre_rate - wrong_penalty
                    cur_rate = max(cur_rate, 1.3)
                    hp.heappush(que, (cur_day, cur_dur, cur_rate))
                else:
                    # 正解だった場合
                    cur_dur = pre_dur * base_rate * easy_bonus
                    cur_day = day + cur_dur
                    cur_rate = pre_rate * easy_bonus
                    hp.heappush(que, (cur_day, cur_dur, cur_rate))
            else:
                # 期日を迎えたカードがない
                ans += 1
                if random.random() >= collect_rate_first:
                    hp.heappush(que, (day+dur_norm, dur_norm, base_rate))
                else:
                    hp.heappush(que, (day+dur_easy, dur_easy, base_rate*easy_bonus))

    print('毎日', num_per_day, '問を', day_last, '日間解くと', ans, '問覚えることができる')
    print('一週間で新たに', ans/day_last*7, '問覚えるペース')
    print('一枚当たり平均', day_last*num_per_day/ans, '回復習する')


main()

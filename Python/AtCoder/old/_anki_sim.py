import heapq as hq


def main():
    sim = []
    hq.heapify(sim)
    ans = []
    new_card = 0
    hq.heappush(sim, [7, 7, 2.5])
    for day in range(1000):
        pre_ans = -1
        if day % 7 == 0:  # 定期的にたまっているカードを全部処理して1枚追加
            if sim[0][0] <= day:
                re_cnt = 0
                while sim[0][0] <= day:
                    re_cnt += 1
                    latest_list = hq.heappop(sim)
                    kankaku = latest_list[1]
                    difficult = latest_list[2]
                    hq.heappush(sim, [day+int(kankaku*difficult), int(kankaku*difficult), int(difficult)])
                pre_ans=re_cnt

                # 学習
                # new_card += 1
                # hq.heappush(sim, [day+7, 7, 2.5])
        else:
            if sim[0][0] <= day:
                # 復習
                latest_list = hq.heappop(sim)
                kankaku = latest_list[1]
                difficult = latest_list[2]
                hq.heappush(sim, [day+int(kankaku*difficult), int(kankaku*difficult), int(difficult)])
                pre_ans=1
            else:
                # 学習
                pre_ans=0
                new_card += 1
                hq.heappush(sim, [day+7, 7, 2.5])
        if day % 7 == 1:  # 毎週土曜日はABC開催のためカード追加
            hq.heappush(sim, [day+7, 7, 2.5])
        ans.append(pre_ans)


    print(ans)
    print(new_card)


main()

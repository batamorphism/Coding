def main():
    n_end, tour_end = map(int, input().split())
    tour = list(map(int, input().split()))
    tour = [t-1 for t in tour]
    cost_of = [tuple(map(int, input().split())) for _ in range(n_end-1)]

    # imos
    # imos[i] += 1 : 都市iで乗車
    # imos[i]: 都市i->i+1の鉄道を使う回数
    imos = [0]*n_end
    for day, fr in enumerate(tour):
        if day == len(tour)-1:
            # 最終日は移動しない
            break
        to = tour[day+1]
        imos[min(fr, to)] += 1
        imos[max(to, fr)] -= 1

    def calc_cost(town, cnt):
        cost1_once, cost2_once, stable_cost = cost_of[town]
        return min(cost1_once*cnt, cost2_once*cnt+stable_cost)

    ans = 0
    cnt = 0
    for town, d_cnt in enumerate(imos):
        cnt += d_cnt
        if cnt != 0:
            ans += calc_cost(town, cnt)
    print(ans)


main()

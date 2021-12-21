# i -> i+1を通る回数を数える
def main():
    node_end, trip_end = map(int, input().split())
    trip = list(map(int, input().split()))
    trip = [town-1 for town in trip]

    cost_list = [tuple(map(int, input().split())) for _ in range(node_end-1)]

    # cnt_of[i] = i -> i+1を通る回数
    cnt_of = [0]*node_end
    set_cnt_of(cnt_of, trip)

    # i -> i+1 を通る回数に応じた運賃
    cost_of = [0]*node_end
    set_cost_of(cost_of, cost_list, cnt_of)

    ans = sum(cost_of)

    print(ans)


def set_cnt_of(cnt_of, trip):
    # 旅行の日程から、i -> i+1を通る回数を数える
    for i in range(len(trip)-1):
        fr = trip[i]
        to = trip[i+1]
        # fr < toとする
        if fr > to:
            fr, to = to, fr
        # [fr, to)に+1すればよい
        cnt_of[fr] += 1
        cnt_of[to] -= 1

    # imos-累積和
    for i in range(1, len(cnt_of)):
        cnt_of[i] += cnt_of[i-1]


def set_cost_of(cost_of, cost_list, cnt_of):
    # i -> i+1を通る回数に応じた運賃を計算
    for fr in range(len(cost_list)):
        cnt = cnt_of[fr]
        a, b, c = cost_list[fr]
        cost1 = a*cnt
        cost2 = b*cnt+c
        cost_of[fr] = min(cost1, cost2)


main()

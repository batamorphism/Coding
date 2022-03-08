import heapq


# 過去の数に+xすることは
# これからの数に-xすることと同じ
# 出力時に、xの総和を加算
def main():
    q = int(input())
    ans_list = []
    sum_val = 0
    que = []
    for _ in range(q):
        query = list(map(int, input().split()))
        query_type = query[0]
        if query_type == 1:
            # x_iを書き込み、袋に入れる
            ball = query[1] + sum_val
            heapq.heappush(que, ball)
        elif query_type == 2:
            # これから入れるボールを、x_i減算する
            x_i = query[1]
            sum_val -= x_i
        elif query_type == 3:
            # 最小のものを出力
            ball = heapq.heappop(que)
            ans = ball - sum_val
            ans_list.append(ans)

    print(*ans_list, sep='\n')


main()

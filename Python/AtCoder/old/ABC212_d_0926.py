import heapq as hq


def main():
    q = int(input())
    query_list = [list(map(int, input().split())) for _ in range(q)]
    que = []
    sum_q2 = 0
    for query in query_list:
        if query[0] == 1:
            # 操作1
            hq.heappush(que, query[1]-sum_q2)
        elif query[0] == 2:
            sum_q2 += query[1]
        else:
            ball = hq.heappop(que)
            print(ball+sum_q2)


main()

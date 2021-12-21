import heapq as hq
# 操作2は、かかれている数に追加ではなく、その後追加するボールから減算する


def main():
    q_end = int(input())
    query_list = []
    for _ in range(q_end):
        query = list(map(int, input().split()))
        query_list.append(query)

    que = []
    sum3 = 0
    for query in query_list:
        p, *x = query
        if p in (1, 2):
            x = x[0]

        if p == 1:
            hq.heappush(que, x-sum3)
        elif p == 2:
            sum3 += x
        else:
            val = hq.heappop(que)
            print(val+sum3)


main()

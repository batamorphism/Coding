import heapq


# 1～k-1番目に大きい値と
# k番目以上に大きい値をそれぞれ別のqueで管理する
def main():
    n, k = map(int, input().split())
    P = list(map(int, input().split()))
    greater_kth = []  # 1~k-1番目に大きい値、先頭はk-1番目に大きい値(最小値)
    lower_kth = []  # k番目以上に大きい値、先頭はk番目に大きい値(最大値)
    # 最初の処理
    for p_i in P[:k-1]:
        heapq.heappush(greater_kth, p_i)

    for p_i in P[k-1:]:
        if greater_kth and p_i >= greater_kth[0]:
            heapq.heappush(greater_kth, p_i)
            kth = heapq.heappop(greater_kth)
            print(kth)
            heapq.heappush(lower_kth, -kth)
        else:
            heapq.heappush(lower_kth, -p_i)
            kth = -lower_kth[0]
            print(kth)


main()

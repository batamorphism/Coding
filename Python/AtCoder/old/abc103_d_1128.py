import heapq as hp


def main():
    n, m = map(int, input().split())
    req_list = []
    for _ in range(m):
        a, b = map(int, input().split())
        req_list.append((a, b))

    req_list.sort()
    que = []
    ans = 0
    for le, ri in req_list:
        if len(que) != 0:
            if que[0][0] <= le:
                # 最小のriがle以下
                # その時点でカットする
                # print(le, ri, que)
                ans += 1
                que = []
        hp.heappush(que, (ri, le))

    if len(que) != 0:
        ans += 1

    print(ans)


main()

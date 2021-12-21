def main():
    q = int(input())
    que = [0]*(q*2+q)
    lo = q
    hi = q
    # デッキは[lo, hi)に存在
    ans_list = []
    for _ in range(q):
        t, x = map(int, input().split())
        if t == 1:
            lo -= 1
            que[lo] = x
        elif t == 2:
            que[hi] = x
            hi += 1
        else:
            # 上から数えてx番目のカードは
            # lo+x-1番目となる
            # print(que, lo, hi, x)
            ans = que[lo+x-1]
            ans_list.append(ans)

    print(*ans_list, sep='\n')


main()

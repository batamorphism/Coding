def main():
    k, t = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    max_a = max(A)
    # max_aは最初からmax_a-1個隣合っている
    # max_aの間にa[1],a[2],...を挟んでいく
    # すると、各a[i]は必ず隣合わないようにできる
    # max_aがとなりあう数を最小にするためには、
    # 各max_aの間に数字を入れていけばいいので
    # これで最小値が求まる
    ans = max_a-1-(k-max_a)
    ans = max(ans, 0)
    print(ans)


main()

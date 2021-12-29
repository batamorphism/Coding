# しゃくとり法
from collections import Counter


def main():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    sum_a = 0
    ans = 0
    counter = Counter()
    counter[0] = 1
    for i, a_i in enumerate(A):
        sum_a += a_i
        cnt = counter[sum_a-k]
        # print(i+1, cnt)
        ans += cnt
        counter[sum_a] += 1
    print(ans)


main()

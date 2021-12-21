mod = 10000


def main():
    n, k = map(int, input().split())
    n_end = n+1
    node_end = 4
    ab_list = [-1]*n_end
    for _ in range(k):
        a, b = map(int, input().split())
        b -= 1
        ab_list[a] = b

    memo = {}

    def calc(day, node1, node2):
        tup = (day, node1, node2)
        if tup in memo:
            return memo[tup]
        # day日目の組み合わせ数で、最終日がnode1、その前日がnode2となる組み合わせ数を返す
        # node1 == 3は、パスタを食べていないことを指す
        if day == 0:
            if node1 == node2 == 3:
                return 1
            else:
                return 0
        else:
            if node1 == 3:
                return 0

        ret = 0
        if ab_list[day] != -1:
            # dayのnodeが最初から決まっている
            if node1 == ab_list[day]:
                for node3 in range(node_end):
                    if not (node1 == node2 == node3):
                        # print(day, node1, node2, node3)
                        ret += calc(day-1, node2, node3)
            memo[tup] = ret % mod
            return ret
        else:  # dayのnodeが最初から決まっていない
            for node3 in range(node_end):
                if not (node1 == node2 == node3):
                    ret += calc(day-1, node2, node3)
            memo[tup] = ret % mod
            return ret

    ans = 0
    for node1 in range(node_end):
        for node2 in range(node_end):
            ans += calc(n, node1, node2)

    print(ans % mod)


main()

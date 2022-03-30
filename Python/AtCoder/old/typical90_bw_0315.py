# 素因数分解
def main():
    n = int(input())
    div_list = []
    # 試し割り法
    while n > 1:
        div = div_of(n)
        div_list.append(div)
        """
        if div != n // div:
            div_list.append(n // div)
        """
        n = n // div
    cnt = len(div_list)
    ans = 0
    while 1 << ans < cnt:
        ans += 1
    print(ans)


def div_of(n):
    # 素数の時はnを返す
    # そうでないときは約数を返す
    for div in range(2, n):
        if div ** 2 > n:
            return n
        if n % div == 0:
            return div
    return n


main()

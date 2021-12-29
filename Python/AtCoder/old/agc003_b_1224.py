# 0が間にない区間について
# 同じカード同士で捨てていって、0か1あまる
# 1は隣に寄せていけるので、0にぶつかるまで、右端を0か1にできる
def main():
    n = int(input())
    A = [int(input()) for _ in range(n)] + [0]

    ans = 0
    sum_a = 0
    for a in A:
        if a == 0:
            # 区間を分割する
            ans += sum_a // 2
            sum_a = 0
        sum_a += a

    print(ans)


main()

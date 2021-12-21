# それぞれの残り枚数は0か1にできる
# 間に0がなければ、1を右端に持っていくことができる
# したがって、0に挟まれた区間のカードの枚数が奇数であれば1枚余り、そうでなければ全部使いきれる
def main():
    n = int(input())
    A = [int(input()) for _ in range(n)] + [0]

    ans = 0
    sum_a = 0
    for a in A:
        if a == 0:
            ans += sum_a - sum_a % 2
            sum_a = 0
        sum_a += a
    print(ans // 2)


main()

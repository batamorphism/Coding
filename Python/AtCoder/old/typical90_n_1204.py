# 最初に左をとるか右をとるか
# a_1, a_2 > b_1, b_2の時
# 組み合わせによらない
# a_1 > b_1 > a_2 > b_2のとき
# a_1とb_1は確定する
def main():
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    ans = 0
    for a, b in zip(A, B):
        ans += abs(a - b)

    print(ans)


main()

mod = 10**9 + 7
rev2 =(mod+1)//2


def main():
    le, ri = map(int, input().split())
    ans = 0
    num = le

    # leを一個足す
    ans += len(str(le))*(le+le)//2
    ans %= mod
    while num < ri:
        bef_num = num+1
        # numを超える最小の10**i-1の形になる数を求める
        for i in range(1, 30):
            if 10**i-1 > num:
                aft_num = 10**i-1
                break
        # ただし、riを超えたらそこまで
        aft_num = min(aft_num, ri)

        # bef_numとaft_numの文字数は同じになる
        # print(bef_num, aft_num, len(str(bef_num)), len(str(aft_num)))
        # print(len(str(bef_num))*(aft_num+bef_num)*(aft_num-bef_num+1)//2)
        ans += len(str(bef_num))*(aft_num+bef_num) % mod * (aft_num-bef_num+1) % mod * rev2
        ans %= mod
        num = aft_num

    print(ans)


main()

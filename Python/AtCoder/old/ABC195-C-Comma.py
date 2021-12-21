# n = 999 -> 0
# n = 999,999 -> 999,000 (999,999 - 999)
# n = 1,000,001 -> 2*(1,000,001 - 999,999) + 999,000
# n = 999,999,999 -> 2*(999,999,999 - 999,999) +999,000 = 1998999999
# n = 999,999,999,999 -> 3*(999,999,999,999 - 999,999,999) + 2*(999,999,999 - 999,999) +999,999

def main():
    n = int(input())
    digits = len(str(n))
    how_many_comma = (digits-1)//3
    # nを下回る、999,999...形態の最大の数値を探す
    max_999_under_n = max_999(n)
    howmany_comma_max_999_under_n = calc_comma_999(max_999_under_n)
    ans = howmany_comma_max_999_under_n + how_many_comma*(n-max_999_under_n)
    print(ans)


def calc_comma_999(n):
    # 999,999,...の形の、9が3の倍数桁並んでいる場合のカンマの数を数える
    digits = len(str(n))
    if n <= 1:
        return 0
    how_many_999 = digits//3  # 999,999 ならば2
    pre_ret = 999*(1000**(how_many_999-1))  # 999,000,000,000のような数値
    pre_n = n // 1000
    return pre_ret*(how_many_999-1) + calc_comma_999(pre_n)


def max_999(n):
    # n以下の最大の999,999,...となる整数を返す
    digits = len(str(n))
    how_many_3numbers = digits//3
    ret = 0
    for num in range(how_many_3numbers+1):
        if n >= (1000**num-1):
            ret = 1000**num-1
        else:
            break
    return ret


main()
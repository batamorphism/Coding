# ポテンシャル
# ab系
# aaa... -> 0回
# baa.. -> 1回
# aba.. -> 2回
#   baa...(1)
# bba.. -> 3回
#   caa...(2)
# aab.. -> 4回
#   bba.. (3)
# bbb.. -> 7回
#   abb(6)
#   bab(5)
#   aab(4)
#   bba(3)


# ac系
# caa -> 2回
#   baa...(1)
# aca -> 4回
#   bba.. (3)
# cca -> 6回
#   bca(5)
#   aca(4)
# aac -> 8回
#   bbb.. (7)


def main():
    n = int(input())
    S = list(input())
    pot = 0
    for i, s_i in enumerate(S):
        if s_i == 'b':
            pot += 2**i
        elif s_i == 'c':
            pot += 2**(i+1)

    print(pot)


main()

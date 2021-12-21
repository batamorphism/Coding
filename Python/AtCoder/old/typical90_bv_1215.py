# ポテンシャルを考える
# aaa... -> 0回
# baa... -> 1回
# aba... -> 2回
# ->baa->aaa
# aab... -> 4回
# -> bba..
# -> caa..(2)

# caa... -> 2回
# -> baa..(1)
# aca... -> 4回
# ->bba...(3)

def main():
    n = int(input())
    S = input()
    pot = 0
    for i, c in enumerate(S):
        if c == 'b':
            pot += 2**i
        if c == 'c':
            pot += 2**i*2

    print(pot)


main()

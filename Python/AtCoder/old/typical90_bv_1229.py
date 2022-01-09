# ポテンシャル
def main():
    n = int(input())
    S = input()
    pot = 0
    for i, s_i in enumerate(S):
        if s_i == 'b':
            pot += pow(2, i)
        elif s_i == 'c':
            pot += pow(2, i+1)
    print(pot)


main()

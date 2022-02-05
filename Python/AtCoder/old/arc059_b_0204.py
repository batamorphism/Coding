# アンバランスな
# aa, aba
# この2パターンのいずれかを含む。
def main():
    S = input()
    s_end = len(S)
    for i, s_i in enumerate(S):
        # check aa
        if i+1 < s_end and S[i+1] == s_i:
            print(i+1, i+2)
            return
        # check aba
        if i+2 < s_end and S[i+2] == s_i:
            print(i+1, i+3)
            return
    print(-1, -1)


main()

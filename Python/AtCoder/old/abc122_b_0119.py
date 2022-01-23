# 全探索
def main():
    S = input()
    n = len(S)
    ans = 0
    for le in range(n):
        for ri in range(le+1, n+1):
            sub_S = S[le:ri]
            if check(sub_S):
                ans = max(ans, len(sub_S))
    print(ans)


def check(S):
    # SがA, C, G, T以外の文字を持たないことの確認
    ACGT = set('ACGT')
    for c in S:
        if c not in ACGT:
            return False
    return True


main()

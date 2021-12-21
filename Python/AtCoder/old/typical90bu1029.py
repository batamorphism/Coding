import sys
sys.setrecursionlimit(10**9)


mod = 10**9+7

def main():
    n = int(input())
    char_list = list(input().split())
    nei_of = [[] for _ in range(n)]
    for _ in range(n-1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        nei_of[a].append(b)
        nei_of[b].append(a)

    # 木DP
    DPA = [1]*n  # head nodeを含む木がaだけを含むときの、分割方法
    DPB = [1]*n  # head nodeを含む木がbだけを含むときの、分割方法
    DPAB = [1]*n  # head nodeを含む木がab両方含むときの
    color = ['w']*n

    def dfs(pre):
        if char_list[pre] == 'a':
            dpa = 1
            dpb = 0
        else:
            dpa = 0
            dpb = 1
        dpall = 1
        for cur in nei_of[pre]:
            if color[cur] != 'w':
                continue
            color[cur] = 'g'
            dfs(cur)
            # これより子ノードはすべて探索済み
            # a->aのみは切ってはいけない:DPA追加
            # a->bのみは切ってもダメ切らなくてもだめ
            # a->a, b両方は切らないとだめ:DPAB追加
            if char_list[pre] == 'a':
                dpa *= (DPA[cur]+DPAB[cur])
                dpa %= mod
            else:
                dpb *= (DPB[cur]+DPAB[cur])
                dpb %= mod
            # a->aのみは切ってはいけないので*1
            # a->bのみは切ってはいけないので*1
            # a->a, b両方は切っても切らなくてもよいので*2
            dpall *= (DPA[cur]+DPB[cur]+DPAB[cur]*2)
            dpall %= mod
        DPA[pre] = dpa
        DPB[pre] = dpb
        DPAB[pre] = (dpall-dpa-dpb) % mod

    color[0] = 'g'
    dfs(0)

    print(DPAB[0] % mod)


main()

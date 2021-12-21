# https://atcoder.jp/contests/typical90/submissions/26224000
import sys
sys.setrecursionlimit(10**9)
mod = 10**9+7


def main():
    n = int(input())
    C = list(input().split())
    nei_of = [[] for _ in range(n)]
    for _ in range(n-1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        nei_of[a].append(b)
        nei_of[b].append(a)

    DP = [[0]*3 for _ in range(n)]
    # DP[pos][0] = 頂点posの部分木を考えたとき、その部分木がaしか含まず、
    # かつ各切断された部分木がa, b両方含むときの組み合わせ
    # DP[pos][1] = bの場合
    # DP[pos][1] = a, b両方含む場合

    color = ['w']*n

    def dfs(pre_node):
        # val1: nodeを含む部分木がa、bのみある状態で、それ以外の切断された部分木がaとb両方含む
        # val2: 題意:nodeを含む部分木の条件は任意で、切断された部分木がaとb両方含むを満たす組み合わせ数
        val1 = 1
        val2 = 1
        for cur_node in nei_of[pre_node]:
            if color[cur_node] != 'w':
                continue
            color[cur_node] = 'g'
            dfs(cur_node)
            if C[pre_node] == 'a':
                val1 *= (DP[cur_node][0]+DP[cur_node][2])
                # 辺を削除する場合は、DP[cur_node][2]のみOK
                # 辺を削除しない場合は、全部OK
                val2 *= (DP[cur_node][0]+DP[cur_node][1]+2*DP[cur_node][2])
            else:
                val1 *= (DP[cur_node][1]+DP[cur_node][2])
                val2 *= (DP[cur_node][0]+DP[cur_node][1]+2*DP[cur_node][2])
            val1 %= mod
            val2 %= mod
        if C[pre_node] == 'a':
            DP[pre_node][0] = val1
            # DP[pre_node][1] = 0  明らかに組み合わせ数は0
            DP[pre_node][2] = (val2-val1) % mod
        else:
            # DP[pre_node][0] = 0  明らかに組み合わせ数は0
            DP[pre_node][1] = val1
            DP[pre_node][2] = (val2-val1) % mod

    color[0] = 'g'
    dfs(0)
    print(DP[0][2])


main()

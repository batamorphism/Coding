import sys
sys.setrecursionlimit(10**6)

# DFS

def main():
    node_end = int(input())
    nei_of = [[] for _ in range(node_end)]
    for _ in range(node_end-1):
        fr, to = map(int, input().split())
        fr -= 1
        to -= 1
        nei_of[fr].append(to)
        nei_of[to].append(fr)
    for nei in nei_of:
        nei.sort()

    done = [False]*node_end
    ans = []

    def dfs(cur, pre):
        done[cur] = True
        ans.append(cur+1)
        for nex in nei_of[cur]:
            if done[nex]:
                continue
            dfs(nex, cur)
            ans.append(cur+1)

    dfs(0, -1)

    print(*ans)


main()

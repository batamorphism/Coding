from collections import defaultdict


def main():
    # クエリ先読み
    n = int(input())
    A = list(map(int, input().split()))
    q = int(input())
    query_list = []
    need_of = [[] for _ in range(n)]
    cnt_of = defaultdict(int)
    for _ in range(q):
        le, ri, x = map(int, input().split())
        le -= 2
        ri -= 1
        query_list.append((le, ri, x))
        need_of[le].append(x)
        need_of[ri].append(x)
    # (le, ri]となる数を求めよ

    # cnt_of[(i, val)] = a_0, ..., a_i までにおける、valの登場数
    d = defaultdict(int)
    for i, a_i in enumerate(A):
        d[a_i] += 1
        for val in need_of[i]:
            cnt_of[(i, val)] = d[val]

    for le, ri, x in query_list:
        # leが-1の時はcnt_of[(le, x)]は存在しない為0となるが、これは正答
        ans = cnt_of[(ri, x)] - cnt_of[(le, x)]
        print(ans)


main()

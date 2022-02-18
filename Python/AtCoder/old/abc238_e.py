from collections import deque


def main():
    n, q = map(int, input().split())
    edge_list = []
    for i in range(q):
        le, ri = map(int, input().split())
        edge_list.append((le, ri+1, i))

    nbh_of = [set() for _ in range(n+10)]
    # le, riに対して、対応するedge_idを返す
    que = deque()
    col = [False] * (q + 1)
    for le, ri, i in edge_list:
        nbh_of[le].add(i)
        nbh_of[ri].add(i)
        if le == 1:
            que.append(i)
            col[i] = True

    # BFSして、riがnに達するか
    max_ri = -1
    while que:
        pre = que.popleft()
        pre_le, pre_ri, pre_i = edge_list[pre]
        max_ri = max(max_ri, pre_ri)
        for cur in nbh_of[pre_le]:
            if col[cur]:
                continue
            col[cur] = True
            cur_le, cur_ri, cur_i = edge_list[cur]
            que.append(cur_i)
            max_ri = max(max_ri, cur_ri)
        for cur in nbh_of[pre_ri]:
            if col[cur]:
                continue
            col[cur] = True
            cur_le, cur_ri, cur_i = edge_list[cur]
            que.append(cur_i)
            max_ri = max(max_ri, cur_ri)

    if max_ri == n + 1:
        print('Yes')
    else:
        print('No')


main()

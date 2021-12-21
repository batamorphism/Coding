# 崩落前の旅の数
# n^(k-1)
# 橋が一個消える

total_count = 0

def main():
    n, m, k, *UV = map(int, open(0).read().split())
    remove_E = [[UV[2*i]-1, UV[2*i+1]-1] for i in range(m)]
    print(remove_E)

    not_neighbor_of = {}
    for e in remove_E:
        v = e[0]
        if v in not_neighbor_of:
            not_neighbor_of[v].append(e[1])
        else:
            not_neighbor_of[v] = [e[1]]
        
        v = e[1]
        if v in not_neighbor_of:
            not_neighbor_of[v].append(e[0])
        else:
            not_neighbor_of[v] = [e[0]]
    
    print(not_neighbor_of[2])

    state = ['w'] * n
    bft(0, 1, n, not_neighbor_of, state, k)

    print(total_count)


def bft(v, cnt, n, not_neighbor_of, state, k):
    global total_count
    if v == 0 and cnt == k:
        total_count += 1
    if cnt >= k:

        return
    for vv in range(n):  # 近隣の都市
        is_neighbor = True
        if not(v in not_neighbor_of):
            is_neighbor = True
        elif (vv in not_neighbor_of[v]):
            is_neighbor = False
        if vv == v:
            is_neighbor = False
        if is_neighbor:
            # if state[vv] == 'w':
            if True:
                state[vv] = 'g'
                cnt += 1
                bft(vv, cnt, n, not_neighbor_of, state, k)
    state[v] = 'b'


main()

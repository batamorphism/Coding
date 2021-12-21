import sys
sys.setrecursionlimit(10000000)


def bft(v):
    global cnt
    global state
    for vv in neighbor_of[v]:
        if state[vv] == 'w':
            state[vv] = 'g'
            cnt += 1
            bft(vv)
    state[v] = 'b'


n, m, *AB_ = map(int, open(0).read().split())
AB = [[AB_[2*i]-1, AB_[2*i+1]-1] for i in range(m)]
V = range(n)
for v in V:
    AB.append([v, v])
neighbor_of = {}
cnt = 0
for e in AB:
    v = e[0]
    if v in neighbor_of:
        neighbor_of[v].append(e[1])
    else:
        neighbor_of[v] = [e[1]]

for start in V:
    state = ['w'] * n
    state[start] = 'b'
    cnt += 1
    bft(start)

print(cnt)

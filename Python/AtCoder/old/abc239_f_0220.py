import heapq
import pypyjit
import sys
sys.setrecursionlimit(10**6)
pypyjit.set_param('max_unroll_recursion=-1')


class UnionFind:
    def __init__(self, n, D):
        self.node_end = n
        self.par = [i for i in range(n)]
        self.D = D[:]  # その連結成分で、足りない次数の総和
        self.useful_node = [[] for _ in range(n)]  # 足りない次数が残っているノード
        for node, d_node in enumerate(D):
            if d_node:
                self.useful_node[node].append((node, d_node))

    def find(self, x):
        if x == self.par[x]:
            return x
        self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if len(self.useful_node[y]) < len(self.useful_node[x]):
            x, y = y, x
        # x側で次数が残っているやつと、y側で次数が残っているやつを返す
        x_side = self.useful_node[x].pop()
        y_side = self.useful_node[y].pop()
        ret = (x_side[0], y_side[0])
        new_x_side = (x_side[0], x_side[1] - 1)
        new_y_side = (y_side[0], y_side[1] - 1)
        if new_x_side[1]:
            self.useful_node[x].append(new_x_side)
        if new_y_side[1]:
            self.useful_node[y].append(new_y_side)
        # yを新たな親に
        self.par[x] = y
        self.D[y] += self.D[x] - 2
        self.D[x] = 0
        for val in self.useful_node[x]:
            self.useful_node[y].append(val)
        self.useful_node[x] = []
        return ret

    def is_same(self, x, y):
        x = self.find(x)
        y = self.find(y)
        return x == y

    def show_all(self):
        done = set()
        for node in range(self.node_end):
            x = self.find(node)
            if x in done:
                continue
            done.add(x)
            yield x

    def get_d(self, x):
        x = self.find(x)
        return self.D[x]


def main():
    node_end, m = map(int, input().split())
    D = list(map(int, input().split()))
    uf = UnionFind(node_end, D)

    if sum(D) != 2*node_end - 2:
        print(-1)
        return

    if min(D) == 0:
        print(-1)
        return

    for _ in range(m):
        a, b = map(lambda x: int(x)-1, input().split())
        if uf.is_same(a, b):
            print(-1)
            return
        uf.union(a, b)

    que_great = []
    que_lower = []
    for node in uf.show_all():
        # 全ての連結成分別に、次数が足りない数が大きいものをヒープで管理
        d_node = uf.get_d(node)
        if d_node != 0:
            heapq.heappush(que_great, (-d_node, node))
            heapq.heappush(que_lower, (d_node, node))

    ans_list = []
    while que_great and que_lower:
        # 次数が足りない数が一番大きいのと、一番小さいのをくっつける
        d_great, great = heapq.heappop(que_great)
        d_lower, lower = heapq.heappop(que_lower)
        d_great *= -1

        if d_great <= 1 or d_lower >= 2:
            # ここで、great==lowerのケースははじかれる
            break

        if uf.is_same(great, lower):
            raise 0
        if d_lower >= 2:
            raise 1
        if great == lower:
            raise 2

        # 次数が2以上足りないgreatと、1足りないlowerをくっつける
        fr, to = uf.union(lower, great)
        ans_list.append((fr+1, to+1))
        # lowerはもう管理する必要ない
        d = uf.get_d(great)
        if d != 0:
            heapq.heappush(que_great, (-d, great))
            heapq.heappush(que_lower, (d, great))

    # 次数が1足りないやつが2つあるか
    last_step = []
    for node in uf.show_all():
        last_step.append((node, uf.get_d(node)))
    if len(last_step) != 2:
        print(-1)
        return
    first = last_step[0]
    second = last_step[1]
    if not (first[1] == 1 and second[1] == 1):
        print(-1)
        return
    fr, to = uf.union(first[0], second[0])
    ans_list.append((fr+1, to+1))

    for ans in ans_list:
        print(ans[0], ans[1])


main()

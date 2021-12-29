# https://kanpurin.hatenablog.com/entry/2021/09/05/163703
# https://ja.wikipedia.org/wiki/%E3%83%88%E3%83%A9%E3%82%A4_(%E3%83%87%E3%83%BC%E3%82%BF%E6%A7%8B%E9%80%A0)#%E4%BA%8C%E5%88%86%E3%83%88%E3%83%A9%E3%82%A4%E6%9C%A8

class BinaryTrie:
    def __init__(self, max_query=2*10**5, bitlen=30):
        n = max_query * bitlen
        self.nodes = [-1] * (2 * n)
        self.cnt = [0] * n
        self.id = 0
        self.bitlen = bitlen

    # xの挿入
    def insert(self,x):
        pt = 0
        for i in range(self.bitlen-1,-1,-1):
            y = x>>i&1
            if self.nodes[2*pt+y] == -1:
                self.id += 1
                self.nodes[2*pt+y] = self.id
            self.cnt[pt] += 1
            pt = self.nodes[2*pt+y]
        self.cnt[pt] += 1

    # 昇順x番目の値
    def kth_elm(self,x):
        pt, ans = 0, 0
        for i in range(self.bitlen-1,-1,-1):
            ans <<= 1
            if self.nodes[2*pt] != -1 and self.cnt[self.nodes[2*pt]] > 0:
                if self.cnt[self.nodes[2*pt]] >= x:
                    pt = self.nodes[2*pt]
                else:
                    x -= self.cnt[self.nodes[2*pt]]
                    pt = self.nodes[2*pt+1]
                    ans += 1
            else:
                pt = self.nodes[2*pt+1]
                ans += 1
        return ans

    # x以上の最小要素が昇順何番目か
    def lower_bound(self,x):
        pt, ans = 0, 1
        for i in range(self.bitlen-1,-1,-1):
            if pt == -1: break
            if x>>i&1 and self.nodes[2*pt] != -1:
                ans += self.cnt[self.nodes[2*pt]]
            pt = self.nodes[2*pt+(x>>i&1)]
        return ans

bt = BinaryTrie()
L,Q = map(int,input().split())
bt.insert(0)
bt.insert(L)
for _ in range(Q):
    c,x = map(int,input().split())
    if c == 1:
        bt.insert(x)
    else:
        p = bt.lower_bound(x)
        print(bt.kth_elm(p)-bt.kth_elm(p-1))
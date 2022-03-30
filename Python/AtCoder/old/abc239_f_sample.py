import sys
readline = sys.stdin.readline
from collections import defaultdict

class UnionFind():
  def __init__(self, n):
    self.n = n
    self.parents = [-1] * n
  def find(self, x):
    if self.parents[x] < 0: return x
    else: self.parents[x] = self.find(self.parents[x]); return self.parents[x]
  def union(self, x, y):
    x = self.find(x); y = self.find(y)
    if x == y: return
    if self.parents[x] > self.parents[y]: x, y = y, x
    self.parents[x] += self.parents[y]
    self.parents[y] = x

  def size(self, x): return -self.parents[self.find(x)]
  def same(self, x, y): return self.find(x) == self.find(y)
  def members(self, x): root = self.find(x); return [i for i in range(self.n) if self.find(i) == root]
  def roots(self): return [i for i, x in enumerate(self.parents) if x < 0]
  def group_count(self): return len(self.roots())
  def all_group_members(self): return {r: self.members(r) for r in self.roots()}
  def __str__(self): return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

n,m = map(int, input().split())
d = list(map(int, input().split()))
ab = [tuple(map(int, readline().split())) for _ in range(m)]

uf = UnionFind(n)
for a,b in ab:
  a -= 1; b -= 1
  if uf.same(a, b):
    print(-1)
    exit()
  uf.union(a, b)
  d[a] -= 1
  d[b] -= 1

# 数が合わなかったらアウト
if 2*m + sum(d) != 2*(n-1):
  print(-1)
  exit()

dct = defaultdict(list)
for i in range(n):
  # d[i]は、iが持っている残りの手の数
  # 手の数がマイナスになってたらアウト
  if d[i] < 0:
    print(-1)
    exit()

  # 要素iの親をkeyにしてdctに要素iを手の数だけ格納
  par = uf.find(i)
  for _ in range(d[i]):
    dct[par].append(i)

# 手が２以上ある塊はmulti_lstに格納
# 手が１つの塊はsingle_lstに格納
multi_lst = []
single_lst = []
for par, lst in dct.items():
  cnt = len(lst)
  if cnt == 1:
    single_lst.append(par)
  elif cnt > 1:
    multi_lst.append((par, cnt))

ans_lst = []
while multi_lst:
  par, cnt = multi_lst.pop()
  child1 = dct[par].pop()
  if single_lst:
    par2 = single_lst.pop()
    child2 = dct[par2].pop()
  else:
    # single_lstに要素がない場合はアウト
    print(-1)
    exit()

  # 実際の頂点番号に戻して答えのリストに格納
  ans_lst.append((child1+1, child2+1))

  # cntが1になったらsingle_lstにparを格納
  # 2以上の場合は、multi_lstにparとcntを格納
  cnt -= 1
  if cnt == 1:
    single_lst.append(par)
  elif cnt > 1:
    multi_lst.append((par, cnt))

# multi_lstがなくなった時、single_lstの要素数が2つであればそれを繋げて終了。
# それ以外の場合はアウト
if len(single_lst) == 2:
  par1 = single_lst[0]
  child1 = dct[par1][0]
  par2 = single_lst[1]
  child2 = dct[par2][0]
  ans_lst.append((child1+1, child2+1))
else:
  print(-1)
  exit()

for ans in ans_lst:
  print(*ans)

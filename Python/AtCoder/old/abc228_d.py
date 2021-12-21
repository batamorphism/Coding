bit_end = 2**21 + 10
bit_data = [0] * (bit_end+10)
A = [-1] * (bit_end+10)
mod = 2**20

def add(pos, x):
    pos += 1
    while pos <= bit_end:
        bit_data[pos] += x
        pos += (pos & -pos)

def get_sum(pos):
    ret = 0
    pos += 1
    while pos > 0:
        ret += bit_data[pos]
        pos -= (pos & -pos)
    return ret

def main():
    for i in range(bit_end):
        add(i, 1)

    q = int(input())
    ans_list = []
    for _ in range(q):
        t, x = map(int, input().split())
        if t == 1:
            xx = x
            x %= mod
            val = get_sum(x-1)
            # get_sum(y) > valとなるyで最小のものを求める
            ok = bit_end
            ng = -1
            while ok-ng > 1:
                mid = (ok+ng) // 2
                if get_sum(mid) > val:
                    ok = mid
                else:
                    ng = mid
            # このときのokが、更新したい最小のインデックス
            ok %= mod
            add(ok, -1)
            add(ok+mod, -1)
            # print('test', val, ok, xx)
            A[ok] = xx
        else:
            x %= mod
            ans = A[x]
            ans_list.append(ans)

    print(*ans_list, sep='\n')


main()

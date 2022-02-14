from collections import deque
import time

def main():
    q = int(input())
    deq = [-1]*(2*q+100)
    # 現在、[cursor_le, cursor_ri)を使用中
    cursor_le = q+50  # 左端の要素
    cursor_ri = q+50  # 右端の要素+1
    ans_list = []
    for _ in range(q):
        t, x = map(int, input().split())
        if t == 1:
            # xをdeqの左に追加
            cursor_le -= 1
            deq[cursor_le] = x
        elif t == 2:
            # xをdeqの右に追加
            cursor_ri += 1
            deq[cursor_ri-1] = x
        else:
            # 左から数えてx番目の要素を取り出す
            target_cursor = cursor_le + x - 1
            ans = deq[target_cursor]
            ans_list.append(ans)

    print(*ans_list)


que = [i for i in range(10**6)]
deq = deque(que)
ans = 0
st_time = time.perf_counter()
for i in range(10**6):
    ans += deq[i]
    if i % 10**5 == 0:
        en_time = time.perf_counter()
        print(i, en_time-st_time)
        st_time = en_time
print(ans)


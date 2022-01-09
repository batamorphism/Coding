from collections import deque
import time


def main():
    que = deque(range(10**8))
    n = len(que) - 1
    ans = 0

    print('get_que[0]')
    start_time = time.perf_counter()
    for _ in range(10**2):
        ans += que[0]
    end_time = time.perf_counter()
    print(end_time - start_time)

    print('get_que[n]')
    start_time = time.perf_counter()
    for _ in range(10**2):
        ans += que[n]
    end_time = time.perf_counter()
    print(end_time - start_time)

    print('get_que[n//2]')
    start_time = time.perf_counter()
    for _ in range(10**2):
        ans += que[n//2]
    end_time = time.perf_counter()
    print(end_time - start_time)


main()

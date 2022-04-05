import time
import sys
from memory_profiler import profile


# @profile()
def main():
    st_t = time.perf_counter()
    l = [[[0]*4 for _ in range(2000)] for _ in range(2000)]
    en_t = time.perf_counter()
    print(en_t - st_t)

    st_t = time.perf_counter()
    l = [[[0]*2000 for _ in range(2000)] for _ in range(4)]
    en_t = time.perf_counter()
    print(en_t - st_t)

    st_t = time.perf_counter()
    for _ in range(1):
        l = [[0]*4 for _ in range(2000*2000)]
    en_t = time.perf_counter()
    print(en_t - st_t)

    st_t = time.perf_counter()
    for _ in range(1):
        l = [[0]*2000 for _ in range(2000*4)]
    en_t = time.perf_counter()
    print(en_t - st_t)


main()

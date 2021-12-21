import array
import time

arr1 = array.array('i')
arr2 = []
arr3 = []

for n_end in [10**3, 10**4, 10**5]:
    print(n_end)
    start = time.time()
    for i in range(n_end):
        arr1.insert(i//2, i)
    elapsed_time = time.time() - start
    print("elapsed_time:{0}".format(elapsed_time) + "[sec]")

    start = time.time()
    for i in range(n_end):
        arr2.insert(i//2, i)
    elapsed_time = time.time() - start
    print("elapsed_time:{0}".format(elapsed_time) + "[sec]")

    start = time.time()
    for i in range(n_end):
        arr3.append(i)
    elapsed_time = time.time() - start
    print("elapsed_time:{0}".format(elapsed_time) + "[sec]")

    print("---")
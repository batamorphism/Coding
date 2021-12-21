def main():
    # input
    n = int(input())
    S = list(map(int, input().split()))
    T = list(map(int, input().split()))
    solv(n, S, T)


def solv(n: int, S: list, T: list):
    """solv
    n人が並んでいて、反時計回りに0,...,n-1の番号が付いている
    i(0<=i<n)番目の人は時刻tに宝石をもらうと、t+S[i]にその宝石をi+1番目に渡す
    また、外部から時刻T[i]にi番目の人に宝石が渡される
    各iに対し、初めて宝石が手渡った時刻を求めよ

    シミュレーションすることを考える
    N<=200,000なので間に合うっぽい
    first_time(i)を、i君が初めてもらう時刻とする
    first_time(i+1) = min(first_time[i]+S[i], T[i])
    ただし、first_time(0) = min(first_time[n-1]+S[n-1], T[n])

    ここで、T[i]のうち最小のものをT[j]として、
    first_time(j) = T[j]
    Args:
        n (int): [description]
        S (list): [description]
        T (list): [description]
    """
    min_i_of_t = n+1
    min_t = 10**24
    for i in range(n):
        if min_t > T[i]:
            min_i_of_t = i
            min_t = T[i]
    first_time = [-1]*n
    # init
    first_time[min_i_of_t] = T[min_i_of_t]
    for i in range(n-1):
        ind = (min_i_of_t + i + 1) % n
        pre_ind = (min_i_of_t + i) % n
        first_time[ind] = min(first_time[pre_ind]+S[pre_ind], T[ind])

    for time in first_time:
        print(time)


main()

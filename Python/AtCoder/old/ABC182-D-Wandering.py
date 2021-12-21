def main():
    # input
    n = int(input())
    A = list(map(int, input().split()))
    solv(n, A)


def solv(n: int, A: list):
    """数直線上の座標0に置かれたロボットが、次の動作をする
    A[0]動く
    A[0],A[1]動く
    A[0],A[1],A[2]動く...
    この時の座標の最大値
    N < 200,000なので実直には無理
    Sum_A[i]をA[0],...,A[i]の総和とする
    Max_Sum_A[i]を、sum_A[0],...,sum_A[i]の最大値とする
    前回の座標xから、x+Max_Sum_A[i]まで最大値を更新した後、x+Sum_A[i]に移動する
    これを繰り返し、x+Max_Sum_A[i]の最大値が答え

    Args:
        n (int): [description]
        A (list): [description]
    """
    # Set Sum_A and Max_Sum_A[i]
    Sum_A = [A[0]]
    Max_Sum_A = [A[0]]
    for i in range(1, n):
        Sum_A.append(Sum_A[i-1]+A[i])
        Max_Sum_A.append(max(Sum_A[i], Max_Sum_A[i-1]))
    # start sim
    ans = 0
    x = 0
    for i in range(n):
        temp_ans = x + Max_Sum_A[i]
        if temp_ans > ans:
            ans = temp_ans
        x += Sum_A[i]
    print(ans)


main()
import random


def _partition(Array: list, p: int, r: int) -> list:
    """パーティション
    Arrayのうち、要素pからrまで（pとrを含む、つまりArray[p:r+1]）について処理する
    パーティションの基準（ピボット）xはArray[r]とする
    戻り値は最終的にxが編集されているインデックスとし
    Arrayの各要素は、戻り値以下の場合はx以下、戻り値以上の場合はx以上となる
    Args:
        Array (list): [description]
        p (int): [description]
        r (int): [description]

    Returns:
        list: [description]
    """
    x = Array[r]
    i = p-1
    for j in range(p, r):
        if Array[j] <= x:
            i += 1
            tmp = Array[i]
            Array[i] = Array[j]
            Array[j] = tmp
    tmp = Array[i+1]
    Array[i+1] = Array[r]
    Array[r] = tmp
    return i+1


def _quicksort(Array, p, r):
    if p < r:
        q = _partition(Array, p, r)
        _quicksort(Array, p, q-1)
        _quicksort(Array, q+1, r)


def quicksort(Array):
    _quicksort(Array, 0, len(Array)-1)


def main():
    A = [random.randint(0, 100000) for i in range(10000)]
    print(A)
    quicksort(A)
    print(A)


main()

# Quick Sort

def partition(A, p, r):
    x = A[r][0]
    i = p - 1
    for j in range(p, r):
        if A[j][0] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q - 1)
        quicksort(A, q + 1, r)


def check_stable(A, B):
    # A_dict[(num, char)] = そのnumに対応するcharがどういう順番で出現したか
    A_dict = {}
    B_dict = {}
    for num, char in A:
        if num not in A_dict:
            A_dict[num] = [char]
        else:
            A_dict[num].append(char)
    for num, char in B:
        if num not in B_dict:
            B_dict[num] = [char]
        else:
            B_dict[num].append(char)

    for num in A_dict:
        if A_dict[num] != B_dict[num]:
            return False

    return True



n = int(input())
A = []
for _ in range(n):
    char, num = input().split()
    num = int(num)
    A.append((num, char))

B = A[:]
quicksort(A, 0, n - 1)
is_stable = check_stable(A, B)

if is_stable:
    print("Stable")
else:
    print("Not stable")

for num, char in A:
    print(char, num)

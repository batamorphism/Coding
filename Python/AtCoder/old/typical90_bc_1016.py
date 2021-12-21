
n, p, q = map(int, input().split())
A = list(map(int, input().split()))
A = [a % p for a in A]
ans = 0
# 添え字が大きいほうから抑えていくと奇麗
for i5 in range(n):
    for i4 in range(i5):
        for i3 in range(i4):
            for i2 in range(i3):
                for i1 in range(i2):
                    if ((((((((A[i1]*A[i2])%p)*A[i3])%p)*A[i4])%p)*A[i5])%p) == q:
                        ans += 1
print(ans)

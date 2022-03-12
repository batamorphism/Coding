// copyright
#include <bits/stdc++.h>
int main() {
    int n, p, q;
    std::cin >> n >> p >> q;
    q %= p;

    std::vector<int64_t> A(n);
    for (int i = 0; i < n; i++) {
        std::cin >> A[i];
    }

    // Aから5個選ぶ
    int ans = 0;
    for (int i1 = 0; i1 < n; i1++) {
        for (int i2 = i1+1; i2 < n; i2++) {
            for (int i3 = i2+1; i3 < n; i3++) {
                for (int i4 = i3+1; i4 < n; i4++) {
                    for (int i5 = i4+1; i5 < n; i5++) {
                        int64_t prod = 1;
                        for (int i : {i1, i2, i3, i4, i5}) {
                            prod *= A[i];
                            prod %= p;
                        }
                        if (prod == q) {
                            ans++;
                        }
                    }
                }
            }
        }
    }

    std::cout << ans << std::endl;

    return 0;
}

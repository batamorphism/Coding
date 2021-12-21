// copyright
#include <bits/stdc++.h>

int main() {
    // 区間DP
    // DP[le][ri] = [le, ri)を落とせるか
    // ri はn+1される

    while (true) {
        // input
        int n;
        std::cin >> n;
        if (n == 0) {
            return 0;
        }
        std::vector<int> w(n);
        for (int i = 0; i < n; i++) {
            std::cin >> w[i];
        }

        int64_t DP[n + 1][n + 1];
        // 初期化

        for (int i = 0; i <= n; i++) {
            for (int j = 0; j <= n; j++) {
                DP[i][j] = 0;
            }
        }

        for (int delta = 0; delta <= n; delta++) {
            for (int le = 0; le <= n; le++) {
                int ri = le + delta;
                if (ri > n) {
                    continue;
                }
                // [le+1, ri-1)を全て落とせる場合
                if (DP[le+1][ri-1] == delta-2) {
                    // leとri-1の差が-1以下ならば落とせる
                    if (abs(w[le] - w[ri-1]) <= 1) {
                        DP[le][ri] = delta;
                        continue;
                    }
                }
                // [le+1, ri-1)を落とせない場合
                // [le, sep), [sep, ri)を落とせるか
                int64_t dp = 0;
                for (int sep = le; sep <= ri; sep++) {
                    dp = std::max(dp, DP[le][sep] + DP[sep][ri]);
                }
                DP[le][ri] = dp;
            }
        }

        int64_t ans = DP[0][n];
        std::cout << ans << std::endl;
    }
}

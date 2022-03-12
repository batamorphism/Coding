// copyright
#include<bits/stdc++.h>

int main() {
    // 貰うDP
    // DP[le][ri]は、[le, ri]を落とすことが可能かどうか
    // 1-indexed
    while (true) {
        int n;
        std::cin >> n;
        if (n == 0) break;
        n++;
        std::vector<std::vector<int>> DP(n, std::vector<int>(n, 0));
        std::vector<int> w(n);
        for (int i = 1; i < n; i++) {
            std::cin >> w[i];
        }
        int ans = 0;
        for (int cnt = 0; cnt <= n; cnt++) {
            for (int le = 1; le < n; le++) {
                int ri = le + cnt - 1;
                if (ri >= n) break;
                if (cnt == 0) {
                    DP[le][ri] = 0;
                    continue;
                }

                int dp = 0;
                // 1. 間をくりぬかれていて、今回、leとriをくりぬく
                if (abs(w[le] - w[ri]) <= 1 && DP[le + 1][ri - 1] == cnt-2) {
                    dp = DP[le + 1][ri - 1] + 2;
                }
                // 2. 途中で分割
                for (int mi = le-1; mi < ri; mi++) {
                    dp = std::max(dp, DP[le][mi] + DP[mi+1][ri]);
                }
                DP[le][ri] = std::max(DP[le][ri], dp);
                std::cout << DP[le][ri] << le << ri << std::endl;
            }
        }
    ans = DP[1][n-1];
    std::cout << ans << std::endl;
    }
    return 0;
}

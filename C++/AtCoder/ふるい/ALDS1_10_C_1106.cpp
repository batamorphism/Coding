// copyright
#include <bits/stdc++.h>
int main() {
    // Longest Common Subsequence
    int q;
    std::cin >> q;
    std::string X;
    std::string Y;
    for (int i = 0; i < q; i++) {
        std::cin >> X >> Y;
        int n = X.size();
        int m = Y.size();
        int DP[n + 1][m + 1];
        for (int i = 0; i <= n; i++) {
            for (int j = 0; j <= m; j++) {
                DP[i][j] = 0;
            }
        }

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                if (X[i - 1] == Y[j - 1]) {
                    DP[i][j] = DP[i - 1][j - 1] + 1;
                } else {
                    DP[i][j] = std::max(DP[i - 1][j], DP[i][j - 1]);
                }
            }
        }
        std::cout << DP[n][m] << std::endl;
    }
}

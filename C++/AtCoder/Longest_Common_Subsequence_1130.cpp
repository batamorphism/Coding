// copyright
#include <bits/stdc++.h>
int main() {
    int q;
    std::cin >> q;
    while (q--) {
        std::string X, Y;
        std::cin >> X >> Y;
        // lcsは1-indexed
        X = '*' + X;
        Y = '*' + Y;

        int x_end = X.size(), y_end = Y.size();
        int DP[x_end][y_end];
        for (int x_i = 0; x_i < x_end; x_i++) {
            for (int y_i = 0; y_i < y_end; y_i++) {
                DP[x_i][y_i] = 0;
            }
        }

        for (int x_i = 1; x_i < x_end; x_i++) {
            for (int y_i = 1; y_i < y_end; y_i++) {
                if (X[x_i] == Y[y_i]) {
                    DP[x_i][y_i] = DP[x_i - 1][y_i - 1] + 1;
                } else {
                    DP[x_i][y_i] = std::max(DP[x_i - 1][y_i], DP[x_i][y_i - 1]);
                }
            }
        }
        int ans = DP[x_end - 1][y_end - 1];
        std::cout << ans << std::endl;
    }
}

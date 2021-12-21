// copyright
#include <bits/stdc++.h>

int main() {
    std::vector<int64_t> ans_list;
    int y_max = 255;
    int y_min = 0;
    int64_t INF = 1e18;

    while (true) {
        int n;
        int m;
        std::cin >> n >> m;
        if (n == 0 && m == 0) {
            break;
        }

        int C[m];
        int X[n];
        for (int i = 0; i < m; i++) {
            std::cin >> C[i];
        }
        for (int i = 0; i < n; i++) {
            std::cin >> X[i];
        }

        int64_t DP[n+1][y_max+1];
        for (int i = 0; i <= n; i++) {
            for (int j = 0; j <= y_max; j++) {
                DP[i][j] = INF;
            }
        }

        DP[0][128] = 0;

        for (int pre_ind = 0; pre_ind < n; pre_ind++) {
            for (int pre_y = 0; pre_y <= y_max; pre_y++) {
                int nex_ind = pre_ind + 1;
                for (auto c : C) {
                    int nex_y;
                    nex_y = pre_y + c;
                    nex_y = std::max(y_min, std::min(y_max, nex_y));
                    DP[nex_ind][nex_y] = std::min(DP[nex_ind][nex_y], DP[pre_ind][pre_y] + (X[nex_ind-1] - nex_y) * (X[nex_ind-1] - nex_y));
                }
            }
        }

        int64_t ans = INF;
        for (int64_t dp : DP[n]) {
            ans = std::min(ans, dp);
        }
        ans_list.push_back(ans);
    }

    for (auto ans : ans_list) {
        std::cout << ans << std::endl;
    }
}

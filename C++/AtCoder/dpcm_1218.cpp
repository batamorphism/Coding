// copyright
#include <bits/stdc++.h>
int main() {
    // DP
    // 配るDPは1-indexed
    // DP[i][val] = y_iを見たときの、末尾valにおける二乗和の最小値
    // DP[i][val] = DP[i-1][val-c_j] + (y_i - val)^2
    int n_end, m_end;
    std::cin >> n_end >> m_end;
    n_end++;
    int val_end = 256;
    int INF = std::numeric_limits<int>::max();
    std::vector DP(val_end, std::vector(n_end, 0));

    std::vector C(m_end, 0);
    std::vector X(m_end, 0);
    for (int i = 0; i < m_end; i++) {
        std::cin >> C[i];
    }
    for (int i = 0; i < n_end; i++) {
        std::cin >> X[i];
    }

    for (int val = 0; val < val_end; val++) {
        DP[0][val] = 0;
    }

    for (int n = 0; n < n_end; n++) {
        for (int val = 0; val < val_end; val++) {
            // 配るDP
            for (auto c_i : C) {
                int nex_val = val + c_i;
                nex_val = std::max(std::min(nex_val, 255), 0);
                int dp = DP[n][val] + (X[n] - val) * (X[n] - val);
                DP[n + 1][nex_val] = std::min(DP[n + 1][nex_val], dp);
            }
        }
    }

    int ans = INF;
    for (int val = 0; val < val_end; val++) {
        ans = std::min(ans, DP[n_end - 1][val]);
    }
    std::cout << ans << std::endl;
}
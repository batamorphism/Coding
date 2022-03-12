// copyright
#include <bits/stdc++.h>

static int64_t memo[5000][5000];

int64_t H(int n, int r) {
    if (memo[n][r] != -1) return memo[n][r];
    if (n <= 0) {
        return 1;
    }
    int nn = n+r-1;
    int rr = r;

}

int64_t rev(int64_t) {
    
}

int main() {
    std::string S;
    std::cin >> S;
    const int64_t MOD = 998244353;
    for (int i = 0; i < 5000; ++i) {
        for (int j = 0; j < 5000; ++j) {
                memo[i][j] = -1;
            }
        }
    }

    int n = S.size();
    int cnt_of[26];
    for (int i = 0; i < 26; i++) {
        cnt_of[i] = 0;
    }

    for (int i = 0; i < n; i++) {
        cnt_of[S[i] - 'a']++;
    }

    int64_t DP[27][n+1];
    for (int c = 0; c < 26; c++) {
        int cnt = cnt_of[c];
        for (int len = 0; len <= n; len++) {
            int dp = 0
            if (1 <= len && len <= cnt) {
                dp = 1;
            }
            for (int i = 0; i <= cnt; i++) {
                if (len - i < 0) {
                    break;
                }
                dp += DP[c-1][len - i] * H(len - i, i);
                dp %= MOD
            }
            DP[c][len] = dp;
        }
    }

    int64_t ans = 0;
    for (int len = 1; len <= n; len++) {
        ans += DP[26][len];
        ans %= MOD;
    }
    std::cout << ans << std::endl;
    return 0;
}

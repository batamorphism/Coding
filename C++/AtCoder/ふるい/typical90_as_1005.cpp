// copyright
#include<bits/stdc++.h>
int main() {
    int n, k;
    const int64_t INF = 1001001001001001001;

    std::cin >> n >> k;
    typedef std::pair<int64_t, int64_t> intpair;
    std::vector<intpair> XY(n);
    for (int i = 0; i < n; i++) {
        std::cin >> XY[i].first >> XY[i].second;
    }
    // 2点間の距離の最大値
    int64_t D_2p[n][n];
    for (int p1 = 0; p1 < n; p1++) {
        for (int p2 = 0; p2 < n; p2++) {
            int64_t x1, y1, x2, y2;
            x1 = XY[p1].first;
            x2 = XY[p2].first;
            y1 = XY[p1].second;
            y2 = XY[p2].second;
            D_2p[p1][p2] = (x1-x2)*(x1-x2)+(y1-y2)*(y1-y2);
        }
    }

    int ALL = 1 << n;
    // 1 group 内での距離の最大値
    int64_t D_bit[ALL];
    for (int bit = 0; bit < ALL; bit++) {
        std::vector<int> p_list;
        for (int i = 0; i < n; i++) {
            if ((bit >> i) & 1) {
                p_list.emplace_back(i);
            }
        }
        int64_t ans = 0;
        for (auto p1 : p_list) {
            for (auto p2 : p_list) {
                ans = std::max(D_2p[p1][p2], ans);
            }
        }
        D_bit[bit] = ans;
    }

    int64_t DP[k+1][ALL];
    for (int gr = 1; gr <= k; gr++) {
        // gr:今いくつのグループを作っているか
        for (int bit = 0; bit < ALL; bit++) {
            // bitの部分集合sub_bitを考える
            // com_bit = bit-sub_bitとする
            // DP[gr][bit] = min(max(DP[gr-1][sub_bit], D_bit[com_bit]))
            if (gr == 1) {
                DP[gr][bit] = D_bit[bit];
                continue;
            }
            int sub_bit = bit;
            int com_bit = 0;
            int64_t ans = INF;
            while (sub_bit > 0) {
                sub_bit--;
                sub_bit = bit&sub_bit;
                com_bit = bit^sub_bit;
                ans = std::min(std::max(DP[gr-1][sub_bit], D_bit[com_bit]), ans);
            }
            DP[gr][bit] = ans;
        }
    }

    int64_t ans;
    ans = DP[k][ALL-1];
    std::cout << ans << std::endl;
}

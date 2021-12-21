// copyright
#include<bits/stdc++.h>


int main() {
    int n, k;
    std::cin >> n >> k;
    std::pair <int64_t, int64_t> points[n];
    int64_t INF = 3*pow(10, 18)+1;
    for (int i = 0; i < n; i++) {
        std::cin >> points[i].first >> points[i].second;
    }

    int64_t dist_2p[n][n];
    for (int p1 = 0; p1 < n; p1++) {
        for (int p2 = 0; p2 < n; p2++) {
            int64_t x1, y1, x2, y2;
            x1 = points[p1].first;
            y1 = points[p1].second;
            x2 = points[p2].first;
            y2 = points[p2].second;
            dist_2p[p1][p2] = (x2-x1)*(x2-x1)+(y2-y1)*(y2-y1);
        }
    }

    int64_t MAX = (1 << n);
    int64_t dist[MAX];
    for (int64_t bit = 0; bit < MAX; bit++) {
        std::vector<int> p_list;
        int64_t d = 0;
        for (int p = 0; p < n; p++) {
            if (bit >> p & 1) {
                p_list.push_back(p);
            }
            for (auto p1 : p_list) {
                for (auto p2 : p_list) {
                    d = std::max(d, dist_2p[p1][p2]);
                }
            }
        }
        dist[bit] = d;
    }

    int64_t DP[MAX][k+1];
    for (int grp = 0; grp < k+1; grp++) {
        for (int64_t bit = 0; bit < MAX; bit++) {
            DP[bit][grp] = INF;
        }
    }
    DP[0][0] = 0;
    for (int grp = 1; grp < k+1; grp++) {
        for (int64_t bit = 1; bit < MAX; bit++) {
            int64_t sub_bit = bit;
            int64_t com_bit = 0;
            while (sub_bit > 0) {
                sub_bit = (sub_bit-1) & bit;
                com_bit = bit ^ sub_bit;
                int64_t dp_dist = std::max(DP[sub_bit][grp-1], dist[com_bit]);
                DP[bit][grp] = std::min(dp_dist, DP[bit][grp]);
            }
        }
    }
    int64_t ans = DP[MAX-1][k];
    std::cout << ans << std::endl;

}

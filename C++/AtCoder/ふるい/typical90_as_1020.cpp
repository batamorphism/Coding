// copyright
#include<bits/stdc++.h>
int main() {
    int64_t INF = 9223372036854775806;
    // input
    int n, k;
    std::cin >> n >> k;
    int64_t XY[n][2];
    for (int i = 0; i < n; i++) {
        int x, y;
        std::cin >> x >> y;
        XY[i][0] = x;
        XY[i][1] = y;
    }

    // calc dist_2p
    int64_t dist_2p[n][n];
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            int64_t x1, y1, x2, y2;
            x1 = XY[i][0];
            y1 = XY[i][1];
            x2 = XY[j][0];
            y2 = XY[j][1];
            dist_2p[i][j] = (x1-x2)*(x1-x2)+(y1-y2)*(y1-y2);
        }
    }

    // calc dist_bit
    // 各bit間の距離の最大値
    int64_t ALL = 1 << n;
    int64_t dist_bit[ALL];
    for (int64_t bit = 0; bit < ALL; bit++) {
        int64_t d = 0;
        std::vector<int> p_list;
        for (int i = 0; i < n; i++) {
            if (bit >> i & 1) {
                p_list.emplace_back(i);
            }
        }
        for (auto p1 : p_list) {
            for (auto p2 : p_list) {
                d = std::max(dist_2p[p1][p2], d);
            }
        }
        dist_bit[bit] = d;
    }

    // solve
    int64_t dist[k+1][ALL];
    // init
    for (int grp = 0; grp <= k; grp++) {
        for (int64_t bit = 0; bit < ALL; bit++) {
            dist[grp][ALL] = INF;
        }
    }
    for (int grp = 1; grp <= k; grp++) {
        for (int64_t bit = 0; bit < ALL; bit++) {
            if (grp == 1) {
                dist[grp][bit] = dist_bit[bit];
                continue;
            }
            int64_t sub_bit = bit;
            int64_t com_bit = 0;
            int64_t d = INF;
            int64_t d_sub = 0;
            while (sub_bit > 0) {
                sub_bit--;
                sub_bit = sub_bit & bit;
                com_bit = bit ^ sub_bit;
                // grp-1のsub_bitにcom_bitを足しこむ
                d_sub = std::max(dist[grp-1][sub_bit], dist_bit[com_bit]);
                d = std::min(d_sub, d);
            }
            dist[grp][bit] = d;
        }
    }
    int64_t ans;
    ans = dist[k][ALL-1];
    std::cout << ans << std::endl;
}

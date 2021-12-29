// copyright
#include <bits/stdc++.h>
int main() {
    int n, k;
    std::cin >> n >> k;
    int grp_end = k+1;

    std::pair<int64_t, int64_t> XY[n];
    for (int i = 0; i < n; ++i) {
        int64_t x, y;
        std::cin >> x >> y;
        XY[i] = std::make_pair(x, y);
    }

    int64_t dist_2p[n][n];
    for (int fr = 0; fr < n; ++fr) {
        for (int to = 0; to < n; ++to) {
            int64_t d;
            int64_t fr_x = XY[fr].first, fr_y = XY[fr].second;
            int64_t to_x = XY[to].first, to_y = XY[to].second;
            d = (fr_x - to_x) * (fr_x - to_x) + (fr_y - to_y) * (fr_y - to_y);
            dist_2p[fr][to] = d;
        }
    }

    int64_t ALL = 1 << n;
    // dist_bit[bit]: bitの距離の最大値
    int64_t dist_bit[ALL];
    for (int64_t bit = 0; bit < ALL; bit++) {
        int64_t d = 0;
        std::vector<int> point_list;
        for (int i = 0; i < n; ++i) {
            if (bit & (1 << i)) {
                point_list.push_back(i);
            }
        }
        for (auto fr : point_list) {
            for (auto to : point_list) {
                d = std::max(d, dist_2p[fr][to]);
            }
        }
        dist_bit[bit] = d;
    }

    // dist[grp][bit]: bitからgrp個に分けたときの、
    // 各グループの距離の最大値の最小値
    int64_t dist[grp_end][ALL];
    for (int grp = 0; grp < grp_end; grp++) {
        for (int64_t bit = 0; bit < ALL; bit++) {
            dist[grp][bit] = 0;
        }
    }

    for (int grp = 1; grp < grp_end; grp++) {
        for (int64_t bit = 0; bit < ALL; bit++) {
            if (grp == 1) {
                dist[grp][bit] = dist_bit[bit];
                continue;
            }
            int64_t d = INT64_MAX;
            int64_t sub_bit = bit;
            int64_t cur_bit = bit ^ sub_bit;
            while (sub_bit != 0) {
                int64_t d_bit = 0;
                sub_bit = bit & (sub_bit - 1);
                cur_bit = bit ^ sub_bit;
                d_bit = std::max(dist[grp-1][sub_bit], dist_bit[cur_bit]);
                d = std::min(d, d_bit);
            }
            dist[grp][bit] = d;
        }
    }

    int64_t ans = dist[k][ALL-1];
    std::cout << ans << std::endl;

    return 0;
}

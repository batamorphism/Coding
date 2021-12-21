// copyright
# include<bits/stdc++.h>

int64_t dfs(int64_t pre_grp, int64_t pre_bit,
            std::vector<std::vector<int64_t>> dist, int64_t dist_bit[]) {
    if (dist[pre_grp][pre_bit] != -1) {
        // 既に探索済み
        return dist[pre_grp][pre_bit];
    }
    if (pre_grp == 1) {
        return dist_bit[pre_bit];
    }
    int64_t cur_bit = pre_bit;
    int64_t com_bit = 0;  // bitの補集合
    int64_t cur_grp = pre_grp-1;
    int64_t d = 4223372036854775806;
    while (cur_bit > 0) {
        cur_bit = pre_bit & (cur_bit-1);
        com_bit = pre_bit ^ cur_bit;
        if (cur_bit == 0 || com_bit == 0) {
            break;
        }
        d = std::min(dfs(cur_grp, cur_bit, dist, dist_bit)+dist_bit[com_bit]
                    , d);
    }
    dist[pre_grp][pre_bit] = d;
    return d;
}

int main() {
    // INPUT
    int n, k;
    std::cin >> n >> k;
    typedef std::pair<int64_t, int64_t> point_t;
    std::vector<point_t> point_list(n);
    for (int i = 0; i < n; i++) {
        std::cin >> point_list[i].first >> point_list[i].second;
    }

    // set dist of bit
    int64_t dist_2p[n][n];
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            point_t x = point_list[i];
            point_t y = point_list[j];
            dist_2p[i][j] = (x.first-y.first)*(x.first-y.first)
                          + (x.second-y.second)*(x.second-y.second);
        }
    }

    int64_t ALL = 1 << n;
    int64_t dist_bit[ALL];
    for (int64_t bit = 0; bit < ALL; bit++) {
        int64_t d = 0;
        std::vector<int> tmp_list;
        for (int i = 0; i < n; i++) {
            if ((bit >> i) & 1) {
                tmp_list.emplace_back(i);
            }
        }
        for (int p1 : tmp_list) {
            for (int p2 : tmp_list) {
                d = std::max(dist_2p[p1][p2], d);
            }
        }
        dist_bit[bit] = d;
    }

    int64_t dist[k+1][ALL];
    for (int64_t grp = 0; grp <= k; grp++) {
        for (int64_t bit = 0; bit < ALL; bit++) {
            dist[grp][bit] = 0;
        }
    }

    for (int64_t grp = 1; grp <= k; grp++) {
        for (int64_t bit = 0; bit < ALL; bit++) {
            if (grp == 1) {
                dist[grp][bit] = dist_bit[bit];
                continue;
            }
            int64_t pre_bit = bit;
            int64_t com_bit = 0;  // bitの補集合
            int64_t pre_grp = grp-1;
            int64_t d = 2000000000000000000;
            while (pre_bit > 0) {
                pre_bit = (pre_bit-1) & bit;
                com_bit = bit ^ pre_bit;
                d = std::min(std::max(dist[pre_grp][pre_bit], dist_bit[com_bit]), d);
            }
            dist[grp][bit] = d;
        }
    }
    int a = dist[1][1];
    std::cout << dist[k][ALL-1] << std::endl;
}

// copyright
#include <bits/stdc++.h>

int main() {
    int n, k;
    std::cin >> n >> k;
    int grp_end = k+1;

    int64_t ALL = 1 << n;

    int64_t X[n];
    int64_t Y[n];
    for (int i = 0; i < n; i++) {
        std::cin >> X[i] >> Y[i];
    }

    // bit全探索
    int64_t dist_2p[n][n];
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            dist_2p[i][j] = (X[i] - X[j])*(X[i] - X[j])
                          + (Y[i] - Y[j])*(Y[i] - Y[j]);
        }
    }

    int64_t dist_bit[ALL];
    for (int bit = 0; bit < ALL; bit++) {
        // 各bit内での距離の最大値を求める
        int64_t max_dist = 0;
        std::vector<int> p_list;
        for (int i = 0; i < n; i++) {
            if ((bit >> i) & 1) {
                p_list.push_back(i);
            }
        }

        for (auto p : p_list) {
            for (auto q : p_list) {
                max_dist = std::max(max_dist, dist_2p[p][q]);
            }
        }

        dist_bit[bit] = max_dist;
    }

    // 各grp, bitの距離の最小値を求める
    int64_t dist[grp_end][ALL];
    for (int bit = 0; bit < ALL; bit++) {
        for (int grp = 0; grp < grp_end; grp++) {
            dist[grp][bit] = std::numeric_limits<int64_t>::max();
        }
    }
    dist[0][0] = 0;

    for (int grp = 1; grp < grp_end; grp++) {
        for (int bit = 0; bit < ALL; bit++) {
            int64_t min_dist = std::numeric_limits<int64_t>::max();
            // grp個のグループを持っている状態での距離の最小値
            // grp-1個のグループ、bitの部分集合sub_bitにおける距離の最小値と、com_bit = bit^sub_bitの距離との最小値
            // が答え
            // ただし、grp = 0の時は0 <- 初期値なので問題なし
            int sub_bit = bit;
            int com_bit = bit ^ sub_bit;
            while (sub_bit) {
                sub_bit--;
                sub_bit &= bit;
                com_bit = bit ^ sub_bit;
                int64_t cur_dist = std::max(dist[grp-1][sub_bit], dist_bit[com_bit]);
                min_dist = std::min(min_dist, cur_dist);
            }

            dist[grp][bit] = min_dist;
        }
    }

    int64_t ans = dist[k][ALL-1];
    std::cout << ans << std::endl;

}

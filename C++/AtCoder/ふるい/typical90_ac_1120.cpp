// copyright
#include <bits/stdc++.h>
int main() {
    int64_t INF = 1 << 30;
    std::deque<std::vector<int>> dq;

    // input
    int r_end, c_end;
    std::cin >> r_end >> c_end;

    int st_r, st_c, en_r, en_c;
    std::cin >> st_r >> st_c >> en_r >> en_c;
    st_r--;
    st_c--;
    en_r--;
    en_c--;

    std::vector<std::string> grid(r_end);

    for (int r = 0; r < r_end; r++) {
        std::cin >> grid[r];
    }

    int dr[4] = {0, 1, 0, -1};
    int dc[4] = {1, 0, -1, 0};

    // 01bfs
    int ori_end = 4;
    int D[r_end][c_end][ori_end];
    for (int r = 0; r < r_end; r++) {
        for (int c = 0; c < c_end; c++) {
            for (int ori = 0; ori < ori_end; ori++) {
                D[r][c][ori] = INF;
            }
        }
    }
    for (int ori = 0; ori < ori_end; ori++) {
        D[st_r][st_c][ori] = 0;
    }

    for (int ori = 0; ori < ori_end; ori++) {
        dq.push_back({st_r, st_c, ori});
    }

    while (!dq.empty()) {
        std::vector<int> pre = dq.front();
        dq.pop_front();
        int pre_r = pre[0];
        int pre_c = pre[1];
        int pre_ori = pre[2];
        for (int cur_ori = 0; cur_ori < ori_end; cur_ori++) {
            int cur_r = pre_r + dr[cur_ori];
            int cur_c = pre_c + dc[cur_ori];
            if (cur_r < 0 || cur_r >= r_end || cur_c < 0 || cur_c >= c_end) {
                continue;
            }
            if (grid[cur_r][cur_c] == '#') {
                continue;
            }
            if (cur_ori == pre_ori) {
                // cost 0
                int pre_d = D[pre_r][pre_c][pre_ori];
                int cur_d = pre_d;
                if (D[cur_r][cur_c][cur_ori] > cur_d) {
                    D[cur_r][cur_c][cur_ori] = cur_d;
                    dq.push_back({cur_r, cur_c, cur_ori});
                }
            } else {
                // cost 1
                int pre_d = INF;
                for (int ori = 0; ori < ori_end; ori++) {
                    pre_d = std::min(pre_d, D[pre_r][pre_c][ori]);
                }
                int cur_d = pre_d + 1;
                if (D[cur_r][cur_c][cur_ori] > cur_d) {
                    D[cur_r][cur_c][cur_ori] = cur_d;
                    dq.push_back({cur_r, cur_c, cur_ori});
                }
            }
        }
    }

    int ans = INF;
    for (int ori = 0; ori < ori_end; ori++) {
        ans = std::min(ans, D[en_r][en_c][ori]);
    }

    std::cout << ans << std::endl;
    return 0;
}

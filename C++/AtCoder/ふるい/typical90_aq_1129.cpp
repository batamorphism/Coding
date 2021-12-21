// copyright
#include <bits/stdc++.h>
int main() {
    // 拡張01bfs
    std::deque<std::vector<int>> que;
    int r_end, c_end;
    std::cin >> r_end >> c_end;

    std::vector<int> st_node(2);
    std::vector<int> en_node(2);
    std::cin >> st_node[0] >> st_node[1];
    std::cin >> en_node[0] >> en_node[1];

    st_node[0]--;
    st_node[1]--;
    en_node[0]--;
    en_node[1]--;

    std::vector<std::string> grid(r_end);
    for (int i = 0; i < r_end; i++) {
        std::cin >> grid[i];
    }

    int ori_end = 4;
    int D[r_end][c_end][ori_end];
    for (int r = 0; r < r_end; r++) {
        for (int c = 0; c < c_end; c++) {
            for (int ori = 0; ori < ori_end; ori++) {
                D[r][c][ori] = std::numeric_limits<int>::max() / 2;
            }
        }
    }

    for (int ori = 0; ori < ori_end; ori++) {
        std::vector<int> tmp(3);
        tmp[0] = st_node[0];
        tmp[1] = st_node[1];
        tmp[2] = ori;
        D[st_node[0]][st_node[1]][ori] = 0;
        que.emplace_back(tmp);
    }

    int dr[] = {0, 1, 0, -1};
    int dc[] = {1, 0, -1, 0};

    while (!que.empty()) {
        auto pre = que.front();
        que.pop_front();
        auto pre_r = pre[0];
        auto pre_c = pre[1];
        auto pre_ori = pre[2];
        auto pre_d = D[pre_r][pre_c][pre_ori];
        // std::cout << pre_r << " " << pre_c << " " << pre_ori << " " << pre_d << std::endl;
        int d;
        int cur_ori, cur_r, cur_c;
        // dist 0 方向の変更なし
        d = pre_d;
        cur_ori = pre_ori;
        cur_r = pre_r + dr[cur_ori];
        cur_c = pre_c + dc[cur_ori];
        if (0 <= cur_r && cur_r < r_end && 0 <= cur_c && cur_c < c_end) {
            if (grid[cur_r][cur_c] == '.') {
                if (D[cur_r][cur_c][cur_ori] > d) {
                    D[cur_r][cur_c][cur_ori] = d;
                    std::vector<int> tmp(3);
                    tmp[0] = cur_r;
                    tmp[1] = cur_c;
                    tmp[2] = cur_ori;
                    que.emplace_front(tmp);
                }
            }
        }

        // dist 1 方向の変更あり
        // 方向転換時は、一個前の向きはどっち向きでもOK
        for (int ori = 0; ori < ori_end; ori++) {
            pre_d = std::min(pre_d, D[pre_r][pre_c][ori]);
        }
        d = pre_d + 1;
        for (int cur_ori = 0; cur_ori < ori_end; cur_ori++) {
            cur_r = pre_r + dr[cur_ori];
            cur_c = pre_c + dc[cur_ori];
            if (0 <= cur_r && cur_r < r_end && 0 <= cur_c && cur_c < c_end) {
                if (grid[cur_r][cur_c] == '.') {
                    if (D[cur_r][cur_c][cur_ori] > d) {
                        D[cur_r][cur_c][cur_ori] = d;
                        std::vector<int> tmp(3);
                        tmp[0] = cur_r;
                        tmp[1] = cur_c;
                        tmp[2] = cur_ori;
                        que.emplace_back(tmp);
                    }
                }
            }
        }
    }
    int ans = std::numeric_limits<int>::max();
    for (int ori = 0; ori < ori_end; ori++) {
        ans = std::min(ans, D[en_node[0]][en_node[1]][ori]);
    }
    std::cout << ans << std::endl;
    /*
    for (int ori = 0; ori < ori_end; ori++) {
        for (int r = 0 ; r < r_end; r++) {
            for (int c = 0; c < c_end; c++) {
                std::cout << D[r][c][ori] << " ";
            }
            std::cout << std::endl;
        }
        std::cout << std::endl;
    }
    */
}

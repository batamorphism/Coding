// copyright
#include<bits/stdc++.h>
int main() {
    int r_end, c_end;
    std::cin >> r_end >> c_end;
    int st_r, st_c, en_r, en_c;
    std::cin >> st_r >> st_c >> en_r >> en_c;
    st_r--;
    st_c--;
    en_r--;
    en_c--;

    std::vector<std::string> grid(r_end);
    for (int i = 0; i < r_end; i++) {
            std::cin >> grid[i];
    }

    int ori_end = 4;
    int dist[r_end][c_end][ori_end];
    int INF = std::numeric_limits<int>::max()/10;

    // 初期化
    for (int i = 0; i < r_end; i++) {
        for (int j = 0; j < c_end; j++) {
            for (int o = 0; o < ori_end; o++) {
                dist[i][j][o] = INF;
            }
        }
    }

    // 0-1BFS
    for (int ori = 0; ori < ori_end; ori++) {
        dist[st_r][st_c][ori] = 0;
    }
    std::deque <std::tuple<int, int, int>> que;
    for (int ori = 0; ori < ori_end; ori++) {
        que.push_back(std::make_tuple(st_r, st_c, ori));
    }

    int dr[ori_end] = {0, 0, 1, -1};
    int dc[ori_end] = {1, -1, 0, 0};

    while (que.size() > 0) {
        auto pre = que.front();
        int pre_r = std::get<0>(pre);
        int pre_c = std::get<1>(pre);
        int pre_o = std::get<2>(pre);
        int pre_d = dist[pre_r][pre_c][pre_o];
        que.pop_front();

        int cur_r, cur_c, cur_o, cur_d;

        // 0-BFS
        cur_r = pre_r + dr[pre_o];
        cur_c = pre_c + dc[pre_o];
        cur_o = pre_o;
        cur_d = pre_d;
        if (0 <= cur_r && cur_r < r_end && 0 <= cur_c && cur_c < c_end) {
            if (grid[cur_r][cur_c] == '.') {
                if (dist[cur_r][cur_c][cur_o] > cur_d) {
                    dist[cur_r][cur_c][cur_o] = cur_d;
                    que.push_front(std::make_tuple(cur_r, cur_c, cur_o));
                }
            }
        }

        // 1-BFS
        for (int o = 0; o < ori_end; o++) {
            cur_r = pre_r + dr[o];
            cur_c = pre_c + dc[o];
            cur_o = o;
            cur_d = pre_d + 1;
            if (0 <= cur_r && cur_r < r_end && 0 <= cur_c && cur_c < c_end) {
                if (grid[cur_r][cur_c] == '.') {
                    if (dist[cur_r][cur_c][cur_o] > cur_d) {
                        dist[cur_r][cur_c][cur_o] = cur_d;
                        que.push_back(std::make_tuple(cur_r, cur_c, cur_o));
                    }
                }
            }
        }
    }

    int ans = INF;
    for (int o = 0; o < ori_end; o++) {
        ans = std::min(ans, dist[en_r][en_c][o]);
    }
    std::cout << ans << std::endl;

    return 0;
}

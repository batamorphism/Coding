// copyright ehekatlact
#include<iostream>
#include<vector>
#include<array>

static int ans = -1;
static std::vector<std::vector<int>> dist;
const std::vector<std::array<int, 2>> drc = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
using Grid = std::vector<std::string>;

void dfs(const int r_end, const int c_end,
         const int pre_r, const int pre_c, const Grid &gird,
         const int st_r, const int st_c) {
    auto pre_d = dist[pre_r][pre_c];
    auto cur_d = pre_d + 1;
    for (auto [dr, dc] : drc) {
        const auto cur_r = pre_r + dr;
        const auto cur_c = pre_c + dc;
        if (cur_r == st_r && cur_c == st_c) {
            // 一周回ってきた場合は、答えになりうる
            if (cur_d > 2) {
                ans = std::max(ans, cur_d);
            }
        }
        if (cur_r < 0 || cur_r >= r_end || cur_c < 0 || cur_c >= c_end) {
            continue;
        }
        if (dist[cur_r][cur_c] != 9999) {
            continue;
        }
        if (gird[cur_r][cur_c] == '#') {
            continue;
        }
        dist[cur_r][cur_c] = cur_d;
        dfs(r_end, c_end, cur_r, cur_c, gird, st_r, st_c);
        dist[cur_r][cur_c] = 9999;
    }
}

int main() {
    int r_end, c_end;
    std::cin >> r_end >> c_end;

    Grid grid(r_end);
    for (auto r = 0; r < r_end; ++r) {
        std::cin >> grid[r];
    }
    // 始点16*16通り別に、16*16頂点のbfsをする
    // O(65535)
    for (auto st_r = 0; st_r < r_end; st_r++) {
        for (auto st_c = 0; st_c < c_end; st_c++) {
            if (grid[st_r][st_c] == '#') {
                continue;
            }
            dist = std::vector<std::vector<int>>(r_end, std::vector<int>(c_end, 9999));
            dist[st_r][st_c] = 0;
            dfs(r_end, c_end, st_r, st_c, grid, st_r, st_c);
        }
    }
    std::cout << ans << std::endl;
}
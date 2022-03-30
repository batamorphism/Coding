// copyright
#include<iostream>
#include<vector>
#include<array>
#include<limits>
#include<deque>

std::array<int, 2> ori2drc(int ori) {
    if (ori == 0) {
        return { 0, 1 };
    } else if (ori == 1) {
        return { 1, 0 };
    } else if (ori == 2) {
        return { 0, -1 };
    } else {
        return { -1, 0 };
    }
}

int main() {
    int r_end, c_end;
    std::cin >> r_end >> c_end;

    int st_r, st_c, en_r, en_c;
    std::cin >> st_r >> st_c >> en_r >> en_c;
    st_r--; st_c--; en_r--; en_c--;

    std::vector<std::string> grid;
    for (int r = 0; r < r_end; r++) {
        std::string row;
        std::cin >> row;
        grid.push_back(row);
    }

    // 01bfs
    // 前回と同じ方向ならコスト0
    // 違う方向ならコスト1
    int int_lim = std::numeric_limits<int>::max()/2;
    std::deque<std::array<int, 3>> que;
    std::vector<std::vector<std::vector<int>>> dist(
        r_end, std::vector<std::vector<int>>(
            c_end, std::vector<int>(4, int_lim)));
    for (int ori = 0; ori < 4; ori++) {
        dist.at(st_r).at(st_c).at(ori) = 0;
        que.push_back({st_r, st_c, ori});
    }

    auto nei_of_cost0 = [=](int pre_r, int pre_c, int pre_ori) {
        std::vector<std::array<int, 3>> nei;
        auto [dr, dc] = ori2drc(pre_ori);
        auto cur_r = pre_r + dr;
        auto cur_c = pre_c + dc;
        if (cur_r < 0 || cur_r >= r_end || cur_c < 0 || cur_c >= c_end) {
            return nei;
        }
        if (grid[cur_r][cur_c] == '#') {
            return nei;
        }
        nei.push_back({cur_r, cur_c, pre_ori});
        return nei;
    };

    auto nei_of_cost1 = [=](int pre_r, int pre_c, int pre_ori) {
        std::vector<std::array<int, 3>> nei;
        for (int ori = 0; ori < 4; ori++) {
            if (ori == pre_ori) continue;
            auto [dr, dc] = ori2drc(ori);
            auto cur_r = pre_r + dr;
            auto cur_c = pre_c + dc;
            if (cur_r < 0 || cur_r >= r_end || cur_c < 0 || cur_c >= c_end) {
                continue;
            }
            if (grid[cur_r][cur_c] == '#') {
                continue;
            }
            nei.push_back({cur_r, cur_c, ori});
        }
        return nei;
    };

    while (que.size() > 0) {
        auto [pre_r, pre_c, pre_ori] = que.front();
        que.pop_front();

        // cost 0
        {
            auto nei = nei_of_cost0(pre_r, pre_c, pre_ori);
            auto pre_d = dist.at(pre_r).at(pre_c).at(pre_ori);
            for (auto [cur_r, cur_c, cur_ori] : nei) {
                if (dist.at(cur_r).at(cur_c).at(cur_ori) > pre_d) {
                    dist.at(cur_r).at(cur_c).at(cur_ori) = pre_d;
                    que.push_front({cur_r, cur_c, cur_ori});
                }
            }
        }

        {
            auto nei1 = nei_of_cost1(pre_r, pre_c, pre_ori);
            auto pre_d = dist.at(pre_r).at(pre_c).at(pre_ori);
            for (auto [cur_r, cur_c, cur_ori] : nei1) {
                if (dist.at(cur_r).at(cur_c).at(cur_ori) > pre_d+1) {
                    dist.at(cur_r).at(cur_c).at(cur_ori) = pre_d+1;
                    que.push_back({cur_r, cur_c, cur_ori});
                }
            }
        }
    }

    auto ans = int_lim;
    for (int ori = 0; ori < 4; ori++) {
        ans = std::min(ans, dist.at(en_r).at(en_c).at(ori));
    }
    std::cout << ans << std::endl;
}

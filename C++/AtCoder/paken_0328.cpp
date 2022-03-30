// copyright
#include<iostream>
#include<vector>
#include<limits>

int color2int(char c) {
    if (c == 'R') return 0;
    if (c == 'B') return 1;
    if (c == 'W') return 2;
    if (c == '#') return -1;
    return -1;
}

int main() {
    int r_end = 5;
    int c_end;
    std::cin >> c_end;

    std::vector<std::vector<int>> grid;
    for (int r = 0; r < r_end; r++) {
        std::vector<int> row;
        std::string c_row;
        std::cin >> c_row;
        for (auto c : c_row) {
            row.push_back(color2int(c));
        }
        grid.push_back(row);
    }

    // DP[col]  現在、col色を使っているときの塗り替えたマスの最小値

    std::vector<int> DP(3, 0);
    for (int c = 0; c < c_end; c++) {
        std::vector<int> new_DP(3, std::numeric_limits<int>::max());

        for (int pre_col = 0; pre_col < 3; pre_col++) {
            for (int cur_col = 0; cur_col < 3; cur_col++) {
                if (pre_col == cur_col) continue;
                // 新たにc列目をcur_col色に染める場合に
                // 塗らなくちゃいけないマスの数
                int cnt = 0;
                for (int r = 0; r < r_end; r++) {
                    if (grid[r][c] != cur_col) {
                        cnt++;
                    }
                }
                new_DP[cur_col] = std::min(new_DP[cur_col], DP[pre_col] + cnt);
            }
        }

        for (int col = 0; col <= 3; col++) {
            DP[col] = new_DP[col];
        }
    }

    int ans = std::numeric_limits<int>::max();
    for (int col = 0; col < 3; col++) {
        ans = std::min(ans, DP[col]);
    }
    std::cout << ans << std::endl;
    return 0;
}

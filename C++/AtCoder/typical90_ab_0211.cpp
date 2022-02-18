// copyright
#include <bits/stdc++.h>

int main() {
    // 2次元imos
    // get input
    int n;
    std::cin >> n;
    int r_end, c_end;
    r_end = 1010;
    c_end = 1010;
    std::vector<std::vector<int>> grid(r_end, std::vector<int>(c_end, 0));
    for (int i = 0; i < n; i++) {
        int lx, ly, rx, ry;
        std::cin >> lx >> ly >> rx >> ry;
        lx++;
        ly++;
        rx++;
        ry++;
        grid[lx][ly]++;
        grid[rx][ly]--;
        grid[lx][ry]--;
        grid[rx][ry]++;
    }

    // 累積和
    for (int r = 0; r < r_end; r++) {
        for (int c = 0; c < c_end; c++) {
            if (r == 0 || c == 0) continue;
            grid[r][c] += grid[r][c-1];
        }
    }

    for (int r = 0; r < r_end; r++) {
        for (int c = 0; c < c_end; c++) {
            if (r == 0 || c == 0) continue;
            grid[r][c] += grid[r-1][c];
        }
    }

    std::vector<int> ans_list(n, 0);
    for (int r = 0; r < r_end; r++) {
        for (int c = 0; c < c_end; c++) {
            int k = grid[r][c];
            if (k == 0) continue;
            ans_list[k-1]++;
        }
    }

    for (auto ans : ans_list) {
        std::cout << ans << std::endl;
    }

    return 0;
}

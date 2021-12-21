// copyright
#include<bits/stdc++.h>
int main() {
    int h, w, r, c;
    std::cin >> h >> w >> r >> c;
    int max_r = h-1;
    int max_c = w-1;
    r--;
    c--;
    std::vector<std::string> matrix(max_r+1);
    for (int r = 0; r <= max_r; r++) {
        std::cin >> matrix[r];
    }
    int dr[4] = {1, 0, -1, 0};
    int dc[4] = {0, 1, 0, -1};
    int ans = 1;  // 自分自身があるので1
    for (int i = 0; i < 4; i++) {
        int cur_r = r;
        int cur_c = c;
        while (1) {
            cur_r += dr[i];
            cur_c += dc[i];
            if (cur_r < 0 || cur_r > max_r || cur_c < 0 || cur_c > max_c) {
                break;
            }
            if (matrix[cur_r][cur_c] == '#') {
                break;
            }
            ans++;
        }
    }
    std::cout << ans << std::endl;
}

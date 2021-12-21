// copyright
# include<bits/stdc++.h>

int main() {
    // input
    int h, w, x, y;
    // swap x and y
    std::cin >> h >> w >> y >> x;
    std::vector<std::string> s(h);
    x--;
    y--;
    for (int i = 0; i < h; i++) {
        std::cin >> s[i];
    }

    // start
    int dx[4] = {+1, +0, -1, -0};
    int dy[4] = {+0, +1, -0, -1};
    int ans = 1;  // s[y][x] is alread watched

    for (int i = 0; i < 4; i++) {
        int curr_x = x;
        int curr_y = y;
        while (1) {
            curr_x += dx[i];
            curr_y += dy[i];
            // out of range
            if (curr_x < 0 || curr_x >= w || curr_y < 0 || curr_y >= h) {
                break;
            }
            // cant watch
            if (s[curr_y][curr_x] == '#') {
                break;
            }
            ans++;
        }
    }

    std::cout << ans << std::endl;
}

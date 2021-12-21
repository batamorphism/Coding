// copyright
# include<bits/stdc++.h>

int main() {
    int h, w, x, y;

    // input
    std:: cin >> h >> w >> x >> y;
    // x軸とy軸を入れ替える
    int tmp;
    tmp = x;
    x = y;
    y = tmp;
    x--;
    y--;
    std::vector<std::string> s(h);
    for (int i = 0; i < h; i++) {
        std::cin >> s[i];
    }

    // 上下左右に動く実装はdxdyを使うと楽
    int dx[4] = {0, 1, 0, -1};
    int dy[4] = {-1, 0, 1, 0};

    int ans = 1;
    for (int i = 0; i < 4; i++) {
        int xx = x;
        int yy = y;
        while (1) {
            xx += dx[i];
            yy += dy[i];
            if (xx < 0 || xx >= w || yy < 0 || yy >= h) break;
            if (s[yy][xx] == '#') break;
            ans++;
        }
    }
    std::cout << ans << std::endl;
}

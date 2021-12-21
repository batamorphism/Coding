// copyright
#include<bits/stdc++.h>

int lcs(std::string x, std::string y) {
    int x_end = x.length();
    int y_end = y.length();
    int DP[x_end][y_end];
    for (int ix = 0; ix < x_end; ++ix) {
        for (int iy = 0; iy < y_end; iy++) {
            DP[ix][iy] = 0;
        }
    }

    // DP[x][y] = x, yまで見たときのlcsの長さ
    // DP[x][y] = DP[x-1][y], DP[x-1][y-1]+1
    for (int ix = 1; ix < x_end; ++ix) {
        for (int iy = 1; iy < y_end; iy++) {
            int dp = 0;
            dp = std::max(DP[ix-1][iy], DP[ix][iy-1]);
            if (x[ix] == y[iy]) {
                dp = DP[ix-1][iy-1]+1;
            }
            DP[ix][iy] = dp;
        }
    }
    return DP[x_end-1][y_end-1];
}

int main() {
    int n;
    std::cin >> n;
    for (int i = 0; i < n; i++) {
        std::string x;
        std::string y;
        std::cin >> x >> y;
        x = '*'+x;
        y = '*'+y;
        int ans = lcs(x, y);
        std::cout << ans << std::endl;
    }
}

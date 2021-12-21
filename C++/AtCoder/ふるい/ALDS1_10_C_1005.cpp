// copyright
#include<bits/stdc++.h>

int lcs(std::string x, std::string y) {
    int max_nx = x.length()+1;
    int max_ny = y.length()+1;
    int DP[max_nx][max_ny];
    for (int nx = 0; nx < max_nx; nx++) {
        for (int ny = 0; ny < max_ny; ny++) {
            if (nx == 0 || ny == 0) {
                DP[nx][ny] = 0;
                continue;
            }
            if (x[nx-1] == y[ny-1]) {
                DP[nx][ny] = DP[nx-1][ny-1]+1;
            } else {
                DP[nx][ny] = std::max(DP[nx][ny-1],
                             std::max(DP[nx-1][ny], DP[nx-1][ny-1]));
            }
        }
    }
    return DP[max_nx-1][max_ny-1];
}

int main() {
    int n;
    std::cin >> n;
    for (int i = 0; i < n; i++) {
        std::string x;
        std::string y;
        std::cin >> x >> y;
        int ans = lcs(x, y);
        std::cout << ans << std::endl;
    }
}

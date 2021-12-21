// copyright
#include<bits/stdc++.h>
int main() {
    int n;
    std::cin >> n;
    std::vector<std::pair<int, int>> p_list(n);
    for (int i = 0; i < n; i++) {
        std::cin >> p_list[i].first >> p_list[i].second;
    }
    int ans = 0;
    for (int i = 0; i < n-1; i++) {
        for (int j = i+1; j < n; j++) {
            int dx, dy;
            auto p1 = p_list[i];
            auto p2 = p_list[j];
            dx = p1.first - p2.first;
            dy = p1.second - p2.second;
            double foo;
            if (dx != 0) {
                foo = (dy+0.)/dx;
            } else {
                foo = 1000000000.;
            }
            if (foo >= -1. && foo <= 1.) {
                ans++;
            }
        }
    }
    std::cout << ans << std::endl;
}

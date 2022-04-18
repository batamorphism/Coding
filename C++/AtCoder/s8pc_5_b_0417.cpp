// copyright
#include<iostream>
#include<vector>
#include<array>
#include<limits>
#include<cmath>
#include<iomanip>

int main() {
    // 最も近い2点間の距離の最小値の半分が答え
    int n, m;
    std::cin >> n >> m;

    using FixedCircle = std::array<int, 3>;
    using FreeCircle = std::array<int, 2>;
    std::vector<FixedCircle> fixed_circle_list(n);
    std::vector<FreeCircle> free_circle_list(m);

    for (int i = 0; i < n; ++i) {
        int x, y, r;
        std::cin >> x >> y >> r;
        fixed_circle_list[i] = FixedCircle{x, y, r};
    }
    for (int i = 0; i < m; ++i) {
        int x, y;
        std::cin >> x >> y;
        free_circle_list[i] = FreeCircle{x, y};
    }

    double ans = std::numeric_limits<double>::max();
    for (auto [x, y, r] : fixed_circle_list) {
        ans = std::min(ans, static_cast<double>(r));
    }
    for (auto [free_x, free_y] : free_circle_list) {
        for (auto [fix_x, fix_y, fix_r] : fixed_circle_list) {
            auto dx = free_x - fix_x;
            auto dy = free_y - fix_y;
            auto d = std::sqrt(dx * dx + dy * dy);
            auto r = d - fix_r;
            ans = std::min(ans, r);
        }

        for (auto [x, y] : free_circle_list) {
            if (x == free_x && y == free_y) {
                continue;
            }
            auto dx = free_x - x;
            auto dy = free_y - y;
            auto d = std::sqrt(dx * dx + dy * dy);
            auto r = d/2;
            ans = std::min(ans, r);
        }
    }
    std::cout << std::fixed << std::setprecision(15) << ans << std::endl;
}

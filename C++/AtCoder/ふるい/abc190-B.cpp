// copyright
#include<bits/stdc++.h>
int main() {
    int n, s, d;
    // 詠唱にs秒未満、威力がdより大
    // 詠唱時間, 威力からなるpair
    std::cin >> n >> s >> d;
    std::vector<std::pair<int, int>> magics(n);
    for (int i = 0; i < n; i++) {
        std::cin >> magics[i].first >> magics[i].second;
    }
    bool damaged = false;
    for (auto magic: magics) {
        if (magic.first < s && magic.second > d) {
            damaged = true;
            break;
        }
    }
    if (damaged) {
        std::cout << "Yes" << std::endl;
    } else {
        std::cout << "No" << std::endl;
    }
}

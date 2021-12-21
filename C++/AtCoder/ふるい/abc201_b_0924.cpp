// copyright
#include<bits/stdc++.h>
int main() {
    int n;
    std::cin >> n;
    std::vector<std::pair<int, std::string>> mount(n);
    for (int i = 0; i < n; i++) {
        std::cin >> mount[i].second >> mount[i].first;
    }
    std::sort(mount.rbegin(), mount.rend());
    std::cout << mount[1].second << std::endl;
}

// copyright
#include<bits/stdc++.h>
int main() {
    int n;
    std::cin >> n;
    std::vector<std::pair<int, int>> s(n);
    for (int i = 0; i < n; i++) {
        std::cin >> s[i].first;
        s[i].second = i+1;
    }
    std::sort(s.begin(), s.end());
    std::cout << s[n-2].second << std::endl;
}

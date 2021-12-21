// copyright
# include<bits/stdc++.h>

int main() {
    int n;
    std::cin >> n;
    std::vector<std::pair<int, std::string>> data(n);
    for (int i = 0; i < n; i++) {
        std::cin >> data[i].second >> data[i].first;
    }
    std::sort(data.begin(), data.end());
    std::cout << data[n-2].second << std::endl;
}

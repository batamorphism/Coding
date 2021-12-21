// copyright
# include<bits/stdc++.h>

int main() {
    int n;
    typedef std::pair<int, std::string> mountain;
    std::cin >> n;
    std::vector<mountain> mountain_list(n);
    for (int i = 0; i < n; i++) {
        std::cin >> mountain_list[i].second >> mountain_list[i].first;
    }
    std::sort(mountain_list.begin(), mountain_list.end());
    mountain ans;
    ans = mountain_list[n-2];
    std::cout << ans.second << std::endl;
}

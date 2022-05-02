// copyright
#include<iostream>
#include<vector>
#include<algorithm>

int main() {
    int64_t n, k;
    std::cin >> n >> k;

    std::vector<int64_t> score_list;
    for (int i = 0; i < n; i++) {
        int64_t a, b, c;
        std::cin >> a >> b;
        c = a - b;
        score_list.push_back(b);
        score_list.push_back(c);
    }
    std::sort(score_list.begin(), score_list.end(), std::greater<int64_t>());

    int64_t ans = 0;
    for (int i = 0; i < k; i++) {
        ans += score_list[i];
    }
    std::cout << ans << std::endl;
}

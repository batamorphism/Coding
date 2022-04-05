// copyright ehekatlact
#include<iostream>
#include<vector>
#include<array>
#include<algorithm>

// 残り時間が尽きるまで、b_iを解き続ける
// そのあと、残り時間が尽きるまでc_i = a_i-b_iを解き続ける
// c_iのほうがb_iより大きい場合は、こちらが優先される

int main() {
    int64_t n, k;
    std::cin >> n >> k;
    std::vector<int64_t> c_list;

    for (int i = 0; i < n; i++) {
        int64_t a, b;
        std::cin >> a >> b;
        auto c = a - b;
        c_list.push_back(c);
        c_list.push_back(b);
    }

    std::sort(c_list.begin(), c_list.end(), std::greater<int64_t>());

    int64_t ans = 0;
    for (auto c_i : c_list) {
        if (k == 0) {
            break;
        }
        ans += c_i;
        k--;
    }

    std::cout << ans << std::endl;
}

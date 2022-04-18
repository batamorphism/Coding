// copyright
#include<iostream>
#include<map>
#include<vector>

using Memo = std::map<int, int>;
static Memo memo;
// nが偶数の場合、nを2で割る
// nが奇数の場合、nに3をかけて1を足す
// これが1に到達するまで繰り返す
int collatz(int p_n) {
    if (memo.find(p_n) != memo.end()) {
        return memo[p_n];
    }
    if (p_n == 1) {
        memo[p_n] = 1;
        return 1;
    }
    int n = p_n;
    std::vector<int> path;
    while (memo.find(n) == memo.end()) {
        if (n % 2 == 0) {
            n /= 2;
        } else {
            n = 3 * n + 1;
        }
        path.emplace_back(n);
    }
    auto len = path.size();
    for (int i = len-1; i > 0; i--) {
        memo[path[i-1]] = memo[path[i]]+1;
    }
    return memo[p_n];
}


int main() {
    constexpr int n_end = 1000001;
    int ans = 0;
    int ans_n = -1;
    for (int n = 1; n <= n_end; n++) {
        auto tmp = collatz(n);
        if (tmp > ans) {
            ans = tmp;
            ans_n = n;
        }
    }
    std::cout << ans_n << " " << ans << std::endl;
}

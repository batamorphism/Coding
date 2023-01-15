// copyright

// include libraries
#include <algorithm>
#include <bitset>
#include <vector>
#include <array>
#include <iostream>
#include <map>
#include <string>
#include <queue>
#include <set>
#include <stack>
#include <tuple>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <cmath>
#include <deque>

int64_t int_pow(int64_t x, int64_t y) {
    int64_t ans = 1;
    for (int i = 0; i < y; i++) {
        ans *= x;
    }
    return ans;
}

int64_t one_step(int64_t x, int64_t k) {
    // 第k桁で四捨五入する
    k++;
    int64_t ans = 0;
    // 切り捨てした後、4か5かで判定
    // xが123, kが0なら、120
    int64_t tmp = x / int_pow(10, k) * int_pow(10, k);
    // xが123, kが0なら、3を返す
    int64_t tmp2 = x % int_pow(10, k) / int_pow(10, k-1);
    if (tmp2 >= 5) {
        tmp += int_pow(10, k);
    }
    return tmp;
}

int main() {
    // 操作は貪欲に繰り返していい
    int64_t x, k;
    std::cin >> x >> k;
    for (int i = 0; i < k; i++) {
        x = one_step(x, i);
    }
    std::cout << x << std::endl;
    return 0;
}
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

int f(int x) {
    if (x == 0) {
        return 1;
    }
    return x*f(x-1);
}

int main() {
    int n;
    std::cin >> n;
    auto ans = f(n);
    std::cout << ans << std::endl;
    return 0;
}

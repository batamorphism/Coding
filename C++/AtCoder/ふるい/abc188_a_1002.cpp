// copyright
#include<bits/stdc++.h>
int main() {
    int x, y;
    std::cin >> x >> y;
    int lo;
    int hi;
    lo = std::min(x, y);
    hi = std::max(x, y);
    if (lo+3 > hi) {
        std::cout << "Yes" << std::endl;
    } else {
        std::cout << "No" << std::endl;
    }
}

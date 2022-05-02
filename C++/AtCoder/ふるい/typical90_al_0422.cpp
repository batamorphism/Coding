// copyright
#include<iostream>
#include<cmath>

int64_t gcd(int64_t a, int64_t b) {
    if (b == 0) {
        return a;
    }
    return gcd(b, a % b);
}

int main() {
    int64_t a, b;
    std::cin >> a >> b;
    auto g = gcd(a, b);
    // 答えは、a*b/g
    a /= g;
    // a*bが10^18を超えるとだめ
    auto ans_float = static_cast<double>(a) * static_cast<double>(b);
    if (ans_float > std::pow(10, 18)+10) {
        std::cout << "Large" << std::endl;
        return 0;
    }

    auto ans = a*b;
    if (ans > 1000000000000000000) {
        std::cout << "Large" << std::endl;
    } else {
        std::cout << ans << std::endl;
    }
}

// copyright
#include<iostream>
#include<vector>

int main() {
    int n, k;
    std::cin >> n >> k;
    std::vector<int> A(n), B(n);
    for (int i = 0; i < n; i++) {
        std::cin >> A[i];
    }
    for (int i = 0; i < n; i++) {
        std::cin >> B[i];
    }

    // 差の絶対値の総和がkを下回ること
    // かつ、kとの差が偶数であること
    int sum = 0;
    for (int i = 0; i < n; i++) {
        auto a_i = A[i];
        auto b_i = B[i];
        sum += std::abs(a_i - b_i);
    }
    if (sum > k) {
        std::cout << "No" << std::endl;
        return 0;
    }
    if ((k - sum) % 2 != 0) {
        std::cout << "No" << std::endl;
        return 0;
    }
    std::cout << "Yes" << std::endl;
    return 0;
}

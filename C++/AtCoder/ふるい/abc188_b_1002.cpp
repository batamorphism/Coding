// copyright
#include<bits/stdc++.h>
int main() {
    int n;
    std::cin >> n;
    std::vector<int64_t> A(n);
    std::vector<int64_t> B(n);
    for (int i = 0; i < n; i++) {
        std::cin >> A[i];
    }
    for (int i = 0; i < n; i++) {
        std::cin >> B[i];
    }
    int64_t ans = 0;
    for (int i = 0; i < n; i++) {
        ans += A[i]*B[i];
    }
    if (ans == 0) {
        std::cout << "Yes" << std::endl;
    } else {
        std::cout << "No" << std::endl;
    }
}

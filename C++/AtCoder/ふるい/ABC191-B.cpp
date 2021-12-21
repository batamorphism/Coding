// copyright
#include<bits/stdc++.h>

int main() {
    int n, x;
    std::cin >> n >> x;
    std::vector<int> A(n);
    std::vector<int> B;
    for (int i = 0; i < n; i++) {
        std::cin >> A[i];
    }

    for (int i = 0; i < n; i++) {
        if (A[i] != x) {
            B.push_back(A[i]);
        }
    }
    for (int ans : B) {
        std::cout << ans << std::endl;
    }
}

// copyright
#include<bits/stdc++.h>
int main() {
    int n;
    int x;
    std::cin >> n >> x;
    std::vector<int> A(n);
    for (int i = 0; i < n; i++) {
        std::cin >> A[i];
    }
    // std::vector<int> ans;
    for (auto a : A) {
        if (a != x) {
            std::cout << a << std::endl;
        }
    }
}
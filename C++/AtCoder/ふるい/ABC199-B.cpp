// copyright
#include<bits/stdc++.h>

int max(int a, int b) {
    if (a >= b) {
        return a;
    } else {
        return b;
    }
}

int main() {
    int n;
    std::cin >> n;
    std::vector<int> A(n);
    std::vector<int> B(n);
    for (int i = 0; i < n; i++) {
        std::cin >> A[i];
    }
    for (int i = 0; i < n; i++) {
        std::cin >> B[i];
    }
    std::sort(A.begin(), A.end());
    std::sort(B.begin(), B.end());
    int ans = 0;
    ans = max(B[0]-A[n-1]+1, 0);
    std::cout << ans << std::endl;
}

// copyright
#include<bits/stdc++.h>
int main() {
    int n;
    std::cin >> n;
    std::vector<std::pair<int, int>> A(n);
    std::vector<std::pair<int, int>> B(n);
    for (int i = 0; i < n; i++) {
        std::cin >> A[i].first >> B[i].first;
        A[i].second = i;
        B[i].second = i;
    }

    std::sort(A.begin(), A.end());
    std::sort(B.begin(), B.end());

    int ans = 0;
    if (A[0].second != B[0].second) {
        // 最も早い従業員が異なる場合
        ans = std::max(A[0].first, B[0].first);
    } else {
        int both_work;
        both_work = A[0].first+B[0].first;
        int b_slow;
        b_slow = std::max(A[0].first, B[1].first);
        int a_slow;
        a_slow = std::max(A[1].first, B[0].first);
        ans = std::min(std::min(both_work, b_slow), a_slow);
    }

    std::cout << ans << std::endl;
}

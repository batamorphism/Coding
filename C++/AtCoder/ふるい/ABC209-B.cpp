// copyright
#include<bits/stdc++.h>

bool solver(int n, int x, std::vector<int> A) {
    /**
     * @brief
     * n個の商品(定価はA[i])が売られている
     * 今日は偶数番目の商品を1円引きで買える
     * 所持金はx円、すべて買えるか
     */
    int curr_money = x;
    for (int i = 0; i < n; i++) {
        if ((i+1)%2 == 0) {  // 偶数番目の商品は1円引き
            curr_money -= A[i]-1;
        } else {
            curr_money -= A[i];
        }
    }
    return curr_money >= 0;
}

int main() {
    // input
    int n, x;
    std::cin >> n >> x;
    std::vector<int> A(n);
    for (int i = 0; i < n; i++) {
        std::cin >> A[i];
    }
    bool ans;
    ans = solver(n, x, A);
    if (ans) {
        std::cout << "Yes" << std::endl;
    } else {
        std::cout << "No" << std::endl;
    }
}

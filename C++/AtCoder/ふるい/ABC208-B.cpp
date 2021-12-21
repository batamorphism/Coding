// Copyright
#include<bits/stdc++.h>

std::vector<int> calc_k_n(int p) {
    int k, n;
    int n_factorial = 1;
    for (int nn = 1;; nn++) {
        if (n_factorial * nn > p) {
            break;
        }
        n_factorial = n_factorial * nn;
    }
    k = p/n_factorial;
    std::vector<int> ans = {k, n_factorial};
    return ans;
}

/**
 * @brief 
 * n!硬貨が流通している
 * P円の商品を、おつりが出ないようにちょうどの金額を支払って買う
 * 最小で何枚の効果が必要か
 * @param p 
 * @return int 
 */
int solver(int p) {
    // あるxに対し、xを下回るk*n!を満たす
    // k, n!の組を返す関数calc_k_n(pp)を作成する
    int pp = p;
    int ans = 0;
    while (true) {
        int k, n_factorial;
        std::vector<int> v(2);
        v = calc_k_n(pp);
        k = v[0];
        n_factorial = v[1];
        if (pp != 0) {
            pp = pp - k*n_factorial;
            ans += k;
        } else {
            break;
        }
    }
    return ans;
}

int main() {
    // input
    int p;
    std:: cin >> p;
    int ans;
    ans = solver(p);
    std::cout << ans << std::endl;
}

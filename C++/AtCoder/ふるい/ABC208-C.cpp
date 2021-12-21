// copyright
#include<bits/stdc++.h>

/**
 * @brief 
 * n人の人がいて、A[i]の番号が割り振られている。
 * ここでA[i]は互いにことなる
 * k個のお菓子を持っている
 * 持っているお菓子がn個以上であれば、全員に1個ずつお菓子を配る
 * そうでない場合は、その時点で持っているお菓子をk'として、番号が小さい順にk'人に1個ずつ配る
 * 全てのお菓子を配った後、i番目の国民は何個のお菓子を持っているか
 * k<=10**18
 * n<=2*10**5
 * O(n)でやる
 * @param n 
 * @param k 
 * @param A 
 */
void solver(int n, int64_t k, std::vector<int> p_A) {
    int k_dash;
    std::vector<int64_t> Ans(n);
    // a[i],iからなる二次元配列を作成する
    std::vector<std::vector<int64_t>> A(n, std::vector<int64_t>(2));
    for (int i = 0; i < n; i++) {
        A[i][0] = p_A[i];
        A[i][1] = i;
    }
    std::sort(A.begin(), A.end());
    int64_t forall;
    // まずは全員に配る処理
    forall = k/n;
    k_dash = k-n*forall;

    // 残りk_dash個は、A[0～k_dash-1][1]に1個づつ配られる
    for (int i = 0; i < n; i++) {
        std::vector<int64_t> a;  // a[0]は通し番号、a[i]は国民番号
        a = A[i];
        if (i <= k_dash-1) {
            Ans[a[1]] = forall+1;
        } else {
            Ans[a[1]] = forall;
        }
    }
    for (int64_t ans : Ans) {
        std::cout << ans << std::endl;
    }

}

int main() {
    // input
    int n;
    int64_t k;
    std::cin >> n >> k;
    std::vector<int> A(n);
    for (int i = 0; i < n; i++) {
        int a;
        std::cin >> a;
        A[i] = a;
    }
    solver(n, k, A);
}

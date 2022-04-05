// copyright
#include<iostream>
#include<vector>

int main() {
    int n;
    std::cin >> n;
    int64_t MOD = 46;

    std::vector<int64_t> A(n), B(n), C(n);
    for (auto pointer : {&A, &B, &C}) {
        auto &array = *pointer;
        for (int i = 0; i < n; i++) {
            std::cin >> array[i];
            array[i] %= MOD;
        }
    }

    int64_t ans = 0;

    // a_i+b_i+c_iがMOD上で0になる
    // O(46**3)
    std::vector<int64_t> A_cnt(MOD), B_cnt(MOD), C_cnt(MOD);
    for (int i = 0; i < n; i++) {
        A_cnt[A[i]]++;
        B_cnt[B[i]]++;
        C_cnt[C[i]]++;
    }
    for (int64_t a_i = 0; a_i < MOD; a_i++) {
        for (int64_t b_i = 0; b_i < MOD; b_i++) {
            for (int64_t c_i = 0; c_i < MOD; c_i++) {
                if ((a_i+b_i+c_i) % MOD == 0) {
                    ans += A_cnt[a_i] * B_cnt[b_i] * C_cnt[c_i];
                }
            }
        }
    }
    std::cout << ans << std::endl;
}

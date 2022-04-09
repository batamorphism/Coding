// copyright
#include<iostream>
#include<vector>
#include<map>

int main() {
    int64_t n;
    std::cin >> n;
    const int64_t MOD = 1000000007;

    std::vector<int64_t> C(n);
    for (int i = 0; i < n; i++) {
        std::cin >> C[i];
    }

    // i番目まで見た場合の組み合わせ数を考える
    // 今まで同じ石が出てきたことがない場合は、DP[i-1]と同じになる
    // 出てきたことがある場合、
    // i番目を選ばなかった場合は、DP[i-1]と同じになる
    // i番目を選んだ場合は、c_iが前回出てきた場所からDP[i-1]までの間は無意味となるので
    // DP[pos[c_i]]となる

    // pos[c_i]は、c_iが前回出てきた場所
    std::map <int64_t, int64_t> pos;
    std::vector<int64_t> DP(n+1);
    DP[0] = 1;

    for (int i = 1; i <= n; i++) {
        auto c_i = C[i-1];
        if (pos.find(c_i) == pos.end()) {
            DP[i] = DP[i-1];
        } else {
            DP[i] = DP[i-1];
            if (pos[c_i] < i-1) {
                DP[i] += DP[pos[c_i]];
            }
        }

        pos[c_i] = i;
        DP[i] %= MOD;
    }
    auto ans = DP[n];
    std::cout << ans << std::endl;
}

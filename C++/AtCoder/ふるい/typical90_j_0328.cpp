// copyright
#include<iostream>
#include<vector>

int main() {
    int n;
    std::cin >> n;
    // score_of[0][i]  1組の学籍番号iの人の点数
    std::vector<std::vector<int>> score_of(2, std::vector<int>(n+1, 0));
    for (int i = 1; i <= n; i++) {
        int c, p;
        std::cin >> c >> p;
        c--;
        score_of[c][i] = p;
    }

    int q;
    std::cin >> q;
    std::vector<int> L(q), R(q);
    for (int i = 0; i < q; i++) {
        std::cin >> L[i] >> R[i];
    }

    // imos
    for (int c = 0; c < 2; c++) {
        for (int i = 1; i <= n; i++) {
            score_of[c][i] += score_of[c][i-1];
        }
    }

    for (int i = 0; i < q; i++) {
        int l = L[i], r = R[i];
        int ans0 = score_of[0][r] - score_of[0][l-1];
        int ans1 = score_of[1][r] - score_of[1][l-1];
        std::cout << ans0 << " " << ans1 << std::endl;
    }

    return 0;
}

// Copyright
#include<bits/stdc++.h>

void solver(int n, std::string s);

int main() {
    // input
    int n;
    std::string s;
    std::cin >> n >> s;
    solver(n, s);
}

void solver(int n, std::string s) {
    /**
     * @brief 
     * n枚のカードをa君とb君が交互に食べる
     * sは01からなる文字列で、1が悪いカードである
     * n<=10^5
     */
    std::string ans;
    for (int i = 0; i < n; ++i) {
        if (s[i] == '1') {
            if (i%2 == 0) {
                // 偶数の時はa君:高橋くんが食べた
                ans = "Takahashi";
            } else {
                ans = "Aoki";
            }
            break;
        }
    }
    std::cout << ans << std::endl;
}

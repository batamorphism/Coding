// Copyright
#include<bits/stdc++.h>

std::vector<int64_t> solver(int64_t n) {
    /**
     * @brief
     * nこのシュークリームがある
     * nを分割することなく平等に分けられる人数としてあり得るもの
     * n=a*bとしたときのaとbを与えればよい
     * ここで、a<bとすれば
     * aを1～n**0.5として、aとn/aを加えればよい
     * a==bの時は、aのみ加えることに注意
     * @return std::vector<int64_t>
     */
    std::vector<int64_t> ans_list;
    for (int64_t i = 1; i <= pow(n, 0.5); i++) {
        if (n%i == 0) {
            ans_list.push_back(i);
            if (i != n/i) {
                ans_list.push_back(n/i);
            }
        }
    }
    std::sort(ans_list.begin(), ans_list.end());
    return ans_list;
}

int main() {
    // input
    int64_t n;
    std::cin >> n;
    // solve
    std::vector<int64_t> ans_list;
    ans_list = solver(n);
    for (int64_t ans : ans_list) {
        std::cout << ans << std::endl;
    }
}

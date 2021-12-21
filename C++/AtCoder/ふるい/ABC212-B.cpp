// Copyright
#include<bits/stdc++.h>

void solver(std::vector<int> x) {
    bool is_weak = false;

    // check1 4桁とも同じ数値である
    int hoge;
    int cnt = 1;
    hoge = x[0];
    for (int i = 1; i < 4; i++) {
        if (x[i] == hoge) {
            cnt += 1;
        }
    }
    if (cnt == 4) {
        is_weak = true;
    }

    // check2 4桁が通し番号である
    int pre_x;
    cnt = 1;
    pre_x = x[0];
    for (int i = 1; i < 4; i++) {
        if (x[i] == (pre_x+1) % 10) {
            cnt += 1;
        }
        pre_x = x[i];
    }
    if (cnt == 4) {
        is_weak = true;
    }

    std::string ans;
    if (is_weak) {
        ans = "Weak";
    } else {
        ans = "Strong";
    }
    std::cout << ans << std::endl;
}

int ctoi(char c) {
    if (c >= '0' && c <= '9') {
        return c-'0';
    }
    return 0;
}

int main() {
    std::string hoge;
    std::cin >> hoge;
    std::vector<int> x(4);
    for (int i = 0; i < 4; i++) {
        char temp = hoge[i];
        x[i] = ctoi(temp);
    }
    solver(x);
}

// copyright
#include <bits/stdc++.h>

bool solver(std::string s) {
    if (s.size() == 1) {
        return s == "8";
    }
    if (s.size() == 2) {
        if (stoi(s) % 8 == 0) {
            return true;
        }
        std::swap(s[0], s[1]);
        return stoi(s) % 8 == 0;
    }
    std::vector<int> cnt(10);  // 1～9がそれぞれいくつあるか
    for (char x : s) {
        int num = 0;
        num = x -'0';
        cnt[num] += 1;
    }
    for (int i = 8*13; i < 1000; i += 8) {
        std::string s_of_8;
        s_of_8 = std::to_string(i);
        std::vector<int> cnt_of_8(10);
        std::vector<int> cnt_minus_cnt_of_8(10);
        for (char x : s_of_8) {
            int num = 0;
            num = x -'0';
            cnt_of_8[num] += 1;  // 1～9がそれぞれいくつあるか
        }
        for (int i=0; i < 10; i++) {
            cnt_minus_cnt_of_8[i] = cnt[i] - cnt_of_8[i];
        }
        bool ret = true;
        for (int x : cnt_minus_cnt_of_8) {
            if (x < 0) {
                ret = false;
            }
        }
        if (ret) {
            return true;
        }
    }
    return false;
}

int main() {
    std::string s;
    std::cin >> s;
    bool is_yes;
    is_yes = solver(s);
    if (is_yes) {
        std::cout << "Yes" << std::endl;
    } else {
        std::cout << "No" << std::endl;
    }
}

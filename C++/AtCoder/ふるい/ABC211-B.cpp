// Copyright (c)
#include<bits/stdc++.h>

void solver(std::vector<std::string> s) {
    bool is_yes = true;
    std::vector<std::string> search_text{"H", "2B", "3B", "HR"};
    for (int i = 0; i < 4; i++) {
        bool temp = false;
        for (int j = 0; j <4; j++) {
            if (search_text[i] == s[j]) {
                temp = true;
            }
        }
        if (!temp) {
            is_yes = false;
        }
    }
    if (is_yes) {
        std::cout << "Yes" << std::endl;
    } else {
        std::cout << "No" << std::endl;
    }
}

int main() {
    // input
    std::vector<std::string> s(4);
    for (int i = 0; i < 4; i++) {
        std::string temp;
        std::cin >> temp;
        s[i] = temp;
    }
    solver(s);
}
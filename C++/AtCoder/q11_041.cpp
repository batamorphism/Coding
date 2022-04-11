// copyright
#include<iostream>
#include<vector>

void show_roman(int n) {
    // (数字, ローマ数字) からなる配列を作成する
    std::vector<std::pair<int, std::string>> roman_nums = {
        {1000, "M"},
        {900, "CM"},
        {500, "D"},
        {400, "CD"},
        {100, "C"},
        {90, "XC"},
        {50, "L"},
        {40, "XL"},
        {10, "X"},
        {9, "IX"},
        {5, "V"},
        {4, "IV"},
        {1, "I"}
    };
    for (auto [num, roman] : roman_nums) {
        while (n >= num) {
            std::cout << roman;
            n -= num;
        }
    }
}

int main() {
    int n = 192;
    show_roman(n);
}
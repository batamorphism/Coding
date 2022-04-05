// copyright
#include<bits/stdc++.h>
std::string to_roman(int64 value) {
    std::vector<std::pair<int64_t, std::string>> const roman {
        {1000, "M"}, {900, "CM"}, {500, "D"},
        {100, "C"}, {90, "XC"}, {50, "L"},
        {10, "X"}, {9, "IX"}, {5, "V"},
        {4, "IV"}, {1, "I"}
    };

    std::string result;
    for (auto const & [num, str] : roman) {
        while (value > num) {
            resutl += str;
            value -= num;
        }
    }
    return result;
}

int main() {
    int64_t n;
    std::cin >> n;
    std::cout << to_roman(n) << std::endl;
    return 0;
}

// copyright
// n 桁の自然数であって、その各桁の数の n 乗の和が、
// 元の自然数に等しくなるような数をいう。
// 例えば、13 + 53 + 33 = 153 であるから、
// 153 はナルシシスト数である。

#include<iostream>

int main() {
    int n_end = 1000;
    int n_begin = 100;
    for (int n = n_begin; n < n_end; n++) {
        int a, b, c;
        a = n/100;
        b = n/10%10;
        c = n%10;
        if (n == (a*a*a + b*b*b + c*c*c)) {
            std::cout << n << std::endl;
        }
    }
}

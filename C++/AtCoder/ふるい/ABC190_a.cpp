//copyright
#include<bits/stdc++.h>
int main() {
    int a, b, c;
    std::cin >> a >> b >> c;
    // 先手の飴をx, 後手の飴をyとする
    // x<yのとき、後手win
    // x=yのとき、後手win
    // x>yのとき、先手win
    std::string first, last;
    int x, y;
    if (c == 0) {
        first = "Takahashi";
        last = "Aoki";
        x = a;
        y = b;
    } else {
        first = "Aoki";
        last = "Takahashi";
        x = b;
        y = a;
    }
    if (x <= y) {
        // 後手の勝利
        std::cout << last << std::endl;
    } else {
        std::cout << first << std::endl;
    }
}

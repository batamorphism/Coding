// copyright
#include<bits/stdc++.h>
int main() {
    int mushi_kokei, nyuusi;
    std::cin >> mushi_kokei >> nyuusi;
    int nyuu_kokei = mushi_kokei+nyuusi;
    int ans;
    if (nyuu_kokei >= 15 && nyuusi >= 8) {
        ans = 1;
    } else if (nyuu_kokei >= 10 && nyuusi >= 3) {
        ans = 2;
    } else if (nyuu_kokei >= 3) {
        ans = 3;
    } else {
        ans = 4;
    }
    std::cout << ans << std::endl;
}

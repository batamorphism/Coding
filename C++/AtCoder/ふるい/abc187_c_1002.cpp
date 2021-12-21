// copyright
#include<bits/stdc++.h>
int main() {
    int a;
    int b;
    std::cin >> a >> b;
    int sa = 0;
    int sb = 0;
    while (a > 0) {
        sa += a % 10;
        a = a/10;
    }
    while (b > 0) {
        sb += b % 10;
        b = b/10;
    }
    std::cout << std::max(sa, sb) << std::endl;
}

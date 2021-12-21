// copyright
#include<bits/stdc++.h>
int main() {
    int v, t, s, d;
    std::cin >> v >> t >> s >> d;
    bool is_invisible;
    is_invisible = (d >= v*t) && (d <= v*s);
    if (is_invisible) {
        std::cout << "No" << std::endl;
    } else {
        std::cout << "Yes" << std::endl;
    }
}

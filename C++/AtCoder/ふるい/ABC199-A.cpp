// copyright
# include<bits/stdc++.h>

int main() {
    int a, b, c;
    std::cin >> a >> b >> c;
    if (std::pow(a, 2)+std::pow(b, 2) < std::pow(c, 2)) {
        std::cout << "Yes" << std::endl;
    } else {
        std::cout << "No" << std::endl;
    }
}

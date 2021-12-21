// copyright
#include<bits/stdc++.h>
int main() {
    std::string C;
    std::cin >> C;
    if (C[0] == C[1] && C[1] == C[2]) {
        std::cout << "Won" << std::endl;
    } else {
        std::cout << "Lost" << std::endl;
    }
}

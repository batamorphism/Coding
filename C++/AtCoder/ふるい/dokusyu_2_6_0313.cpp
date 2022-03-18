// copyright
#include<iostream>
#include<string>
int main() {
    std::string n;
    while (true) {
        std::cout << "TYPE" << std::endl;
        std::getline(std::cin, n);
        if (n == "") {
            break;
        }
    }
    return 0;
}

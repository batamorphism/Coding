// copyright
#include<string>
#include<iostream>

int main() {
    std::string text = "hello world";
    for (auto c : text) {
        std::cout << c << std::endl;
    }
    return 0;
}

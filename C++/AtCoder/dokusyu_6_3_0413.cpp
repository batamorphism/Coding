// copyright
#include<iostream>
#include<utility>

void f(int& val) {
    std::cout << "f(int& val) called" << std::endl;
}

void f(int&& val) {
    std::cout << "f(int&& val) called" << std::endl;
}

int main() {
    int val = 1;
    f(val);
    f(std::move(val));
}

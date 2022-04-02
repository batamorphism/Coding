// copyright
#include<iostream>

int f1() {
    return 1;
}

int f2() {
    return 2;
}

int main() {
    #define f1 f2
    std::cout << f1() << std::endl;
    #undef f1
}

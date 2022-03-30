// copyright
#include<iostream>

int main() {
    int i = 0;
    int* p = &i;
    *p = 42;
    std::cout << i << std::endl;
}

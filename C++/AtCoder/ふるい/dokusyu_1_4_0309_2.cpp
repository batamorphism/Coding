// copyright
#include<iostream>

int main() {
    int a = 3;
    if (a+1 == 1) {
        std::cout << "a+1 is 1" << std::endl;
    } else if (a+1 == 2) {
        std::cout << "a+1 is 2" << std::endl;
    } else if (a+1 == 3) {
        std::cout << "a+1 is 3" << std::endl;
    } else {
        std::cout << "a+1 is not 1 or 2 or 3" << std::endl;
    }
    return 0;
}

// copyright
#include<iostream>

int gcd(int a, int b) {
    if (a == 0) {
        return b;
    }
    return gcd(b % a, a);
}

int lcm(int a, int b) {
    return a/gcd(a, b)*b;
}

int main() {
    int a = 3*5*7;
    int b = 2*3*5*11;
    std::cout << lcm(a, b) << std::endl;
}

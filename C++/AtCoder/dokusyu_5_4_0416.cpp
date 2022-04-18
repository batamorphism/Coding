// copyright
#include<iostream>

class A {
    int v;
 public:
    explicit A(int v) : v(v) {
        std::cout << 1 << std::endl;
    }
    A() {
        std::cout << 0 << std::endl;
    }
    friend int get(const A& a);
};

int main() {
    auto a = new A[10] {
        A(1),
        A(2),
        A(3),
     };
}

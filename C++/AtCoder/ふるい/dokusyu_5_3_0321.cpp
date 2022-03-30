// copyright
#include<iostream>

class A {
    int val = 0;
 public:
    A(int v) : val(v) {
        std::cout << "A::A(int v)" << std::endl;
    }
    ~A() {
        std::cout << "A::~A()" << std::endl;
    }
    int get() { return val; }
};

int main() {
    A* ptr = new A(2);
    std::cout << ptr->get() << std::endl;
    delete ptr;
    return 0;
}

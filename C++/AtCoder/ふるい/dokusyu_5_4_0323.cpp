// copyright
#include<iostream>

class A {
    int val = 0;
 public:
    A() {
        std::cout << "A::A()" << std::endl;
    }
    explicit A(const int val) {
        std::cout << "A::A(const int val)" << std::endl;
        this->val = val;
    }
    ~A() {
        std::cout << "A::~A()" << std::endl;
    }
};

int main() {
    A* a = new A;
    A* b = new A(1);

    delete a;
    delete b;
}

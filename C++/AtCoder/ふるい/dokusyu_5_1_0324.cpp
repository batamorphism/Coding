// copyright
#include<iostream>
#include<memory>

class A {
    int value = 0;
 public:
    A() {
        std::cout << "A()" << std::endl;
    }
    ~A() {
        std::cout << "~A()" << std::endl;
    }
};

std::unique_ptr<A> allocate(int n) {
    std::unique_ptr<A> p(new A);
    return p;
}

int main() {
    auto a = allocate(5);
}

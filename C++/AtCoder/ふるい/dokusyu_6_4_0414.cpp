// copyright
#include<iostream>
#include<memory>

class A {
    int a;
 public:
    A() : a(0) {}
    explicit A(int a) : a(a) {}
    int get_a() { return a; }
    ~A() { std::cout << "A::~A()" << std::endl; }
};

class B {
    A a;
 public:
    B() {
        a = A(1);
    }
    std::unique_ptr<A> use_unique_ptr() {
        std::unique_ptr<A> ptr(new A(2));
        return ptr;
    }
};

int main() {
    B b;
    auto ptr = b.use_unique_ptr();
}
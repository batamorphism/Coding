// copyright
#include<iostream>

class A {
 public:
    virtual void foo() = 0;
};

class B : A {
 public:
    void foo() final {
        std::cout << "B::foo()" << std::endl;
    }
};

class C : B {
 public:
    void foo() final {
        std::cout << "C::foo()" << std::endl;
    }
};
}

int main() {
    B b;
    b.foo();
}

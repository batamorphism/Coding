// copyright
#include<iostream>
#include<memory>
#include<utility>

class A {
 public:
    explicit A(std::string name) {
        std::cout << "A " << name << std::endl;
    }
};

class B : virtual public A {
 public:
    B() : A("B") {
        std::cout << "B()" << std::endl;
    }
};

class C : virtual public A {
 public:
    C() : A("C") {
        std::cout << "C()" << std::endl;
    }
};

class D : public B, public C {
 public:
    D() : A("D") {
        std::cout << "D()" << std::endl;
    }
};


int main() {
    using D_ptr = std::unique_ptr<D>;
    // std::unique_ptr<D> d(new D());
    auto ptr = D_ptr{new D()};
}

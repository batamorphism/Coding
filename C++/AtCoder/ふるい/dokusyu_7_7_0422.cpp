#include<iostream>

class A {
 public:
    explicit A(std::string name) {
        std::cout << "A" << name << std::endl;
    }
    ~A() {
        std::cout << "~A" << std::endl;
    }
};

class B : virtual public A {
 public:
    B() : A("B") {
        std::cout << "B" << std::endl;
    }
};

class C : virtual public A {
 public:
    C() : A("C") {
        std::cout << "C" << std::endl;
    }
};

class D : public B, public C {
 public:
    D() : A("D") {
        std::cout << "D" << std::endl;
    }
};

int main() {
    D d;
    return 0;
}

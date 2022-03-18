// copyright
#include<iostream>
class Base {
 public:
    void show();
};

void Base::show() {
    std::cout << "Base::show()" << std::endl;
}

class Derived : public Base {
 public:
    // using Base::show;
    void show(int value);
};

void Derived::show(int value) {
    std::cout << "Derived::show(int value)" << std::endl;
}

int main() {
    Derived d;
    d.show();
    d.show(1);
    return 0;
}

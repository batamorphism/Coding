// copyright
#include<iostream>

class A {
    int v;
 public:
    void set(int value);
    const int& get() const;
    int& get();
};

void A::set(int value) {
    A::v = value;
}

const int& A::get() const {
    return A::v;
}

int& A::get() {
    return A::v;
}

int main() {
    A a;
    a.set(42);
    const A& ca = a;
    std::cout << ca.get() << std::endl;
}

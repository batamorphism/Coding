// copyright
#include<iostream>

class A {
    static int p;
 public:
    void const set_value(int val) {
        p = val;
    }
    int get_value() const {
        return p;
    }
};

int A::p = 1;

int main() {
    A a;
    a.set_value(10);
    std::cout << a.get_value() << std::endl;
    return 0;
}

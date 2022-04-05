// copyright
#include<iostream>

class A {
    static int value;
 public:
    void set(int v) const {
        value = v;
    }
    int get() const {
        return value;
    }
};

int A::value = 0;

int main() {
    const auto a = A();
    a.set(1);
    std::cout << a.get() << std::endl;
    return 0;
}
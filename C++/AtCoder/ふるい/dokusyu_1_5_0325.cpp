// copyright
#include<iostream>
#include<utility>

class A {
    int value = 0;
 public:
    explicit A(int value) : value(value) {}
    int getValue() const { return value; }
    A(const A& other) {
        value = other.value;
        std::cout << "copy constructor" << std::endl;
    }
    A(A&& other) {
        value = other.value;
        std::cout << "move constructor" << std::endl;
    }
};

void show(int&& rref) {
    std::cout << rref << std::endl;
}

int main() {
    A a = A(42);
    A b = A(a);
    A c = A(std::move(a));
}

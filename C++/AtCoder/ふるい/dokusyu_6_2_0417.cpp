// copyright
#include<iostream>

class A {
 public:
    A() {
        std::cout << "A::A()" << std::endl;
    }
    A(const A& other);
};

A::A(const A& other) {

}

int main() {
    A a;
}

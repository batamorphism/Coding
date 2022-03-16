// copyright
#include<iostream>

class A {
    static int counter;
 public:
    A();
    static int get_counter();
};

int A::counter = 0;

A::A() {
    counter++;
}

int A::get_counter() {
    return counter;
}

int main() {
    A a;
    A b;
    A c;
    std::cout << a.get_counter() << std::endl;
    return 0;
}
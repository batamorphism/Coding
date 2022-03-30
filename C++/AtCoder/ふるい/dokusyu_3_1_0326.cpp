// copyright
#include<iostream>
#include<utility>

class MyLongNameClass {
    using integer = int;
    integer value = 42;
 public:
    void setter(integer value);
    integer getter();
};


void MyLongNameClass::setter(integer value) {
    this->value = value;
}

MyLongNameClass::integer MyLongNameClass::getter() {
    return value;
}

int main() {
    using A = MyLongNameClass;
    A a = A();
    std::cout << a.getter() << std::endl;
}

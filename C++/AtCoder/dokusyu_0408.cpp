// copyright
#include<iostream>
#include<utility>

class A {
 public:
    A() {
        std::cout << "A()" << std::endl;
    }
    explicit A(int value) {
        std::cout << "A(int)" << std::endl;
    }
    ~A() {
        std::cout << "~A()" << std::endl;
    }
};

int main() {
    A* array = new A[5]{
        A(),
        A(1),
        A(2),
    };
    delete [] array;
}

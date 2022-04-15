// copyright
#include<iostream>

class A {
 public:
    A() {
        std::cout << "A()" << std::endl;
    }
    A(int val) {
        std::cout << "A(int val)" << std::endl;
    }
    ~A() {
        std::cout << "~A()" << std::endl;
    }
};

int main() {
    A* array = new A[10] {
        A(1),
    };

    delete [] array;
}

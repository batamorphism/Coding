// copyright
#include<iostream>

class A {
 public:
    A() {
        std::cout << "test" << std::endl;
    }
    explicit A(int i) {
        std::cout << "test1" << std::endl;
    }
    A(int i, int j) {
        std::cout << "test2" << std::endl;
    }
    ~A() {
        std::cout << "test3" << std::endl;
    }
};

int main() {
    A* array = new A[10]{
        A(),
        A(1),
        A(1, 2),
    };

    delete array;
}
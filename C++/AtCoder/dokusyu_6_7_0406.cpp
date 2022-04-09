// copyright
#include<iostream>
#include<memory>

class A {
    int value = 0;
 public:
    A() {
        std::cout << "test" << std::endl;
    }
    explicit A(int val) {
        std::cout << "test1" << std::endl;
    }
    explicit A(int val, int val2) {
        std::cout << "test2" << std::endl;
    }
    ~A() {
        std::cout << "test4" << std::endl;
    }
};

int main() {
    A* array = new A[10]{
        A(),
        A(1),
        A(1, 2),
    };

    delete [] array;
}
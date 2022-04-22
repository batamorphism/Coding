// copyright
#include<iostream>

class A {
 public:
    A() {}
    explicit A(int a) {
        std::cout << "test1" << std::endl;
    }
    A(int a, int b) {
        std::cout << "test2" << std::endl;
    }

    ~A() {
        std::cout << "test3" << std::endl;
    }
};

int main() {
    auto a = new A();
    auto b = new A(1);
    auto c = new A(1, 2);

    auto array = new A[5]{
        A(),
        A(1),
        A(1, 2)
    };

    delete [] array;
}

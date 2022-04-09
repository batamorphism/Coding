// copyright
#include<iostream>
#include<vector>

class A {
    static int count;
 public:
    A() {
        std::cout << "c" << std::endl;
        count++;
    }
    ~A() {
        std::cout << "d" << std::endl;
        count--;
    }
    static int getCount() {
        return count;
    }
};

int A::count = 0;

int main() {
    A* array = new A[10] {
        A(),
        A(),
        A(),
        A()
    };
    delete [] array;
}

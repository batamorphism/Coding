// copyright
#include<iostream>
class A {
 private:
    int a = 42;
    friend void display(const A& a);
};

// メンバ関数ではないけど、friendとして宣言されているので、
void display(const A& a) {
    std::cout << a.a << std::endl;
}

int main() {
    A a;
    display(a);
}

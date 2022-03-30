// copyright
#include<iostream>

class A {
    int m_v;
 public:
    explicit A(int v): m_v(v) {}
    int v() const { return m_v; }
};

int main() {
    A a(1);
    std::cout << a.v() << std::endl;
}

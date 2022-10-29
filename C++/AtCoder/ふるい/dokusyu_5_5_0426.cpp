// copyright
#include<iostream>

class A {
 public:
    virtual void hoge() {
        std::cout << "hoge" << std::endl;
    }
};

class B : public A {
 public:
    void hoge() override {
        std::cout << "hogehoge" << std::endl;
    }
};

int main() {
    A a;
    B b;
    a.hoge();
    b.hoge();
}

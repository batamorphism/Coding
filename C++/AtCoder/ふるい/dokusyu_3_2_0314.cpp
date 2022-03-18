// copyright
#include<iostream>

class Base {
 public:
    virtual std::string name() const {
        return "Base";
    }
    virtual std::string most_name() const;
};

class Derived : public Base {
 public:
    std::string name() const override {
        return "Derived";
    }
    std::string most_name() const override {
        return "Derived";
    };
};

int main() {
    Derived d;
    std::cout << d.most_name() << std::endl;
    return 0;
}

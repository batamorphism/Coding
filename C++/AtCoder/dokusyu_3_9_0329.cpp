// copyright
#include<iostream>

class Base {
 public:
    virtual std::string name() const;
    virtual std::string more_name() const = 0;
};

std::string Base::name() const {
    return "Base";
}

class Derived : public Base {
 public:
    virtual std::string name() const;
};

std::string Derived::name() const {
    return "Derived";
}

class MoreDerived : public Derived {
 public:
    virtual std::string name() const;
    virtual std::string more_name() const;
};

std::string MoreDerived::name() const {
    return "MoreDerived";
}

std::string MoreDerived::more_name() const {
    return "MORE_MoreDerived";
}

int main() {
    MoreDerived d;
    std::cout << d.name() << std::endl;
}

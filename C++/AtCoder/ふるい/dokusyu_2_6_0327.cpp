// copyright
#include<iostream>

class LONGNAME {
    int v;
 public:
    void set(int value);
    const int get() const;
};

using A = LONGNAME;

int main() {
    A a;
    a.set(1);
    std::cout << a.get() << std::endl;
    return 0;
}


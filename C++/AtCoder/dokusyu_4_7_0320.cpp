// copyright
#ifndef HEADER_GUARD_DOKUSYU_4_7_0320
#define HEADER_GUARD_DOKUSYU_4_7_0320
#include<iostream>

namespace A::B::C {
    int val = 42;
}

int main() {
    namespace abc = A::B::C;
    std::cout << abc::val << std::endl;
    return 0;
}
#endif

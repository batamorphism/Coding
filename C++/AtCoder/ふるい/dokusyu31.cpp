#include <iostream>

namespace module {
    void method() {
        std::cout << "Hello, world!" << std::endl;
    }
}

void method() {
    std::cout << "Hello, world!2" << std::endl;
}

int main() {
    using module::method;
    //module::method();
    method();
}
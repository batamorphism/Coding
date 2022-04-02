// copyright
#include<iostream>

void enumerate(int* first, int* last, void (*func)(int)) {
    for ( ; first != last; ++first) {
        func(*first);
    }
}

int main() {
    int array[] = {1, 2, 3, 4, 5};

    auto len = sizeof(array)/sizeof(array[0]);
    auto last = array + len;

    auto show = [](int v) {
        std::cout << v << std::endl;
    };

    enumerate(array, last, show);
}

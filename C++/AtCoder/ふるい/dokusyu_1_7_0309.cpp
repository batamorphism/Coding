// copyright
#include<iostream>

int main() {
    int array[] = {4, 2, 1, 9, 5};
    int i = 5;
    do {
        i--;
        std::cout << array[i] << std::endl;
    } while (i > 0);
    return 0;
}

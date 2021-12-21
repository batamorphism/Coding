// copyright
# include<bits/stdc++.h>

int main() {
    int n;
    std::cin >> n;
    //打ち切り除算は、
    //0～99 -> 0
    //100～199 -> 1
    //
    int century;
    century =(n-1)/100+1;
    std::cout << century << std::endl;
}

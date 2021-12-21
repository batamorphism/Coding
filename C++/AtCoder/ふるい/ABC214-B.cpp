// Copyright ???
#include<bits/stdc++.h>
#include <iostream>

int main() {
    int s, t;
    int ans = 0;
    std::cin >> s >> t;
    for (int a = 0; a < s+1; a++)
        for (int b=0; b < s+1; b++)
            for (int c = 0; c < s+1; c++)
                if ((a+b+c) <= s && (a*b*c) <= t) {
                    ans+=1;
                } else {
                    break;
                }
    std::cout << ans << std::endl;
}

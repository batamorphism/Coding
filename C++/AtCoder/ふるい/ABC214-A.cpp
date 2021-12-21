#include<bits/stdc++.h>
using namespace std;
int main(){
    int n,m = 6;
    cin >> n;
    if(n<126){
        m=4;
    }
    else if(n>211){
        m=8;
    }
    cout<<m;
}
#include <iostream>
#include <map>
#include <algorithm>
using namespace std;

int main(void)
{
  int n, a;
  map<int, int> mp;
  
  cin >> n;
  for(int i = 1; i <= n; i++) cin >> a, mp[a]++;

    // mapを逆順に捜査する
    for(auto [key, value] : reverse(mp)) {
      cout << key << " " << value << endl;
    }
  return 0;
}

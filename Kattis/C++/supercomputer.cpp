#include <iostream>
#include <vector>
using namespace std;

// Code for segment tree taken from http://codeforces.com/blog/entry/18051
const int N = 1e6; 
int n; 
int t[2 * N];

void build() {  
  for (int i = n - 1; i > 0; --i) t[i] = t[i<<1] + t[i<<1|1];
}

void modify(int p, int value) {  
  for (t[p += n] = value; p > 1; p >>= 1) t[p>>1] = t[p] + t[p^1];
}

int query(int l, int r) {  
  int res = 0;
  for (l += n, r += n; l < r; l >>= 1, r >>= 1) {
    if (l&1) res += t[l++];
    if (r&1) res += t[--r];
  }
  return res;
}


int main() {
  int queries;
  char a;
  int one,two;
  cin >> n >> queries;
  for (int i = 0; i < n; i++) 
  	t[n+i]=0;

  for(int i = 0; i< queries; i++)
  {
  	cin >> a;
  	if (a=='F')
  	{
  		cin >> one;
  		one--;
  		if (t[n+one]==0)
  			modify(one,1);
  		else
  			modify(one,0);
  	}
  	else
  	{
  		cin >> one >> two;
  		one--;
  		printf("%d\n",query(one,two));
  	}
  }

}
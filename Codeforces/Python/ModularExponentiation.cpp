#include <iostream>
using namespace std;

int main()
{
	int m;
	int n;
	int x = 1;
	cin >> n;
	cin >> m;

	for (int i = 0; i < n; i++)	
		x *= 2;

	int result = m % x;

	cout << result;
}
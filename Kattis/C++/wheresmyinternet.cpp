#include <iostream>
using namespace std;

#define MAXN 200000
int p[MAXN];
int find(int x)
{
	return p[x] == x ? x: p[x] = find(p[x]);
}

void unite (int x, int y)
{
	p[find(x)] = find(y);
}

int main()
{
	int houses;
	int connections;
	cin >> houses >> connections;

	for(int x = 0; x<houses;x++)
	{
		p[x]=x;
	}

	for(int x=0; x<connections;x++)
	{
		int temp1,temp2;
		cin >> temp1 >> temp2;
		unite(temp1-1,temp2-1);
	}

	bool output = false;

	for(int x=1; x<houses;x++)
	{
		if(find(0)!=find(x))
		{
			cout << x+1 << '\n';
			output = true;
		}
	}

	if (output == false)
		cout << "Connected";
}
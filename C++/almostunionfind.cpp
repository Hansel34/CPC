#include <iostream>
using namespace std;

#define MAXN 200200
int p[MAXN];
long long total[MAXN];
int cont[MAXN];
int find(int x)
{
	return p[x] == x ? x: p[x] = find(p[x]);
}

void unite (int x, int y)
{
	if(find(x)!=find(y))
	{
		total[find(x)]+=total[find(y)];
		cont[find(x)]+= cont[find(y)];
		p[find(y)] = find(x);
	}
}

void change (int x, int y)
{
	if(find(x)!=find(y))
	{
	total[find(y)]-= (y+1);
	total[find(x)]+= (y+1);
	cont[find(y)]--;
	cont[find(x)]++;
	p[y]=find(x);
	}
}

int main()
{
	int n,m;

	while(cin >> n >> m)
	{
		for (int i = 0, j = n; i < n; i++, j++) 
		{
			p[i] = j;
			p[j] = j;
			cont[j] = 1;
			total[j]= i+1;
		}

		for (int i = 0; i < m; i++)
		{
			int one,two,three;
			cin >> one >> two;
			if (one==1)
			{
				cin >> three;
				unite(two-1,three-1);
			}
			if (one==2)
			{
				cin >> three;
				change(three-1,two-1);

			}
			if (one==3)
			{
				cout << cont[find(two-1)] << " " << total[find(two-1)] << '\n';
			}
		}
	}

}
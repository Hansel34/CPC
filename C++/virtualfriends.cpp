#include <iostream>
#include <map>
using namespace std;

#define MAXN 200100
int p[MAXN];
int cont[MAXN];
int cnt;

int find(int x)
{
	return p[x] == x ? x: p[x] = find(p[x]);
}

void unite (int x, int y)
{
	if(find(x)!=find(y))
	{
	cont[find(y)]+= cont[find(x)];
	p[find(x)] = find(y);
	}
}

int main()
{
	int n;
	cin >> n;

	while(n--)
	{
		int testcases;
		int counter = 0;
		string friend1,friend2;
		cin >> testcases;
		for (int i = 0; i < testcases*2; i++) 
		{
			p[i] = i;
			cont[i] = 1;
		}


		map <string,int>  friends;
		while (testcases--)
		{
			cin >> friend1 >> friend2;

			if(friends.count(friend1)== 0)
			{
				friends[friend1]=counter;
				counter++;
			}
			if(friends.count(friend2)== 0)
			{
				friends[friend2]=counter;
				counter++;
			}

			unite(friends[friend1],friends[friend2]);
			cout<<cont[find(friends[friend2])] << "\n";
	


		}
	}


}
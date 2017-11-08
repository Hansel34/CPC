#include <iostream>
#include <vector>
using namespace std;

int main()
{
	int n,m;
	int Case = 1;

	while(cin >> n)
	{
		cout <<"Case " <<Case << ":\n";
		vector <int> lst;
		vector<int> total;

		for(int i=0;i<n;i++)
		{
			int temp;
			cin >> temp;
			lst.push_back(temp);
		}

		for(int i=0;i<n;i++)
		{
			for(int y=i+1;y<n;y++)
			{
				total.push_back(lst[i]+lst[y]);
			}

		}

		cin >> m;

		for (int i=0;i<m;i++)
		{
			int temp;
			int output=1000000000;
			cin >> temp;
			for (int i = 0; i<total.size();i++)
			{
				if(abs((temp-total[i]))< abs(temp-output))
				{
					output = total[i];
				}
			}
			cout << "Closest sum to " << temp << " is "<<output<<".\n";
		}
		Case++;

	}

	
	
}

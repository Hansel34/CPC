#include <iostream>
#include <stack>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
	int testCase;
	int numMovies;
	int numRequests;
	vector <int> movies;
	cin >> testCase;

	for (int x = 0; x< testCase; x++)
	{
		cin >> numMovies >> numRequests;
		for (int y = 0; y < numMovies;y++)
		{
			movies.push_back(y);
		}
		for (int a = 0; a< numRequests; a++)
		{
			int request;
			cin >> request;

			vector<int>::iterator it;

			it = find (movies.begin(),movies.end(), )

		}
	}
}
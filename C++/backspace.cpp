#include <iostream>
#include <stack>
#include <vector>
using namespace std;

int main()
{
	stack<char> myqueue;
	string c;
	cin >> c;
	vector<char> output;

	for(int x=0; x<c.size();x++)
	{
		if (c[x] == '<')
			myqueue.pop();
		else
			myqueue.push(c[x]);
	}
	int size = myqueue.size();
	for (int x = 0; x<size;x++)
	{
		output.push_back(myqueue.top());
		myqueue.pop();
	}
	for(int x=0; x<output.size();x++)
	{
		cout << output[size-x-1];
	}
}
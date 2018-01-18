#include <iostream>
using namespace std;

int main()
{
	int tasks, lengthTime, taskTime, totalTime, taskDone;

	cin>> tasks>>lengthTime;

	totalTime = 0;
	taskDone = 0;

	for(int x = 0;x<tasks;x++)
	{
		cin >> taskTime;
		if (totalTime+taskTime>lengthTime)
			break;
		totalTime+=taskTime;
		taskDone++;

	}
	cout << taskDone;

	
}
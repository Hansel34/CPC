#include<iostream>
#include<vector>
#include<string>

using namespace std;
int main()
{
    int length;
    string num;
    cin >> length;
    cin >> num;

    vector<int> nonZeros;
    int zeroes = 0;

    for(char c : num)
    {
        if (c != '0')
        {
            int newNum = c-'0';
            newNum = newNum % 3;
            nonZeros.push_back( c-'0');
        }
        else
        {
            zeroes+=1;
        }
    }

    length -= zeroes;

    long long sum = 0;
    for (int x : nonZeros) 
    {
        sum += x; 
    }
    


    vector<vector<long long> > dp(length + 1, vector<long long>(sum + 1, 0)); 

    for (int i = 0; i <= length; i++)  
        dp[i][0]++; 

    for (int i = 1; i <= length; i++) { 
        dp[i][nonZeros[i - 1]]++; 
        for (int j = 1; j <= sum; j++) { 
  
            if (dp[i - 1][j] > 0) { 
                dp[i][j]++; 
                dp[i][j + nonZeros[i - 1]]++; 
            } 
        } 
    } 

    int count = 0; 
    for (int j = 1; j <= sum; j++) 
  
        // Check if the sum exists 
        if (dp[length][j] > 0) 
  
            // check sum is divisible by m 
            if (j % 3 == 0) 
                count += dp[length][j]; 
    cout << count + count*zeroes; 

}
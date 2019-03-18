#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int n, m;
    cin >> n >> m;
    vector<int> weight;
    vector<int> value;

    int item_weight;
    int item_value;
    for (int i = 0; i < n; i++)
    {
        cin >> item_weight >> item_value;
        weight.push_back(item_weight);
        value.push_back(item_value);
    }
    int p = 1 << n;
    int max_val = 0;
    int curr_weight, curr_value;

    for (int i = 0; i < p; i++) {
        curr_weight = 0;
        curr_value = 0 ;
        for (int j = 0; j < n; j++) {
            if ((i >> j) & 1) {
                curr_weight+=weight[j];
                if (curr_weight <= m)
                {
                    curr_value += value[j];
                    if (curr_value > max_val)
                        max_val = curr_value;
                }
                else
                {
                    if (curr_value > max_val)
                        max_val = curr_value;
                }

            }
        }
    }

    cout << max_val << endl;
}



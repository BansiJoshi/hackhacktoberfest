#include <iostream>

using namespace std;

int main()
{
    int n,i;

    cout<<"Enter the range to find sum:";
    cin >> n;

    int sum = 0;

    for(i=0; i<=n; i++)
    {
            if(i%2 == 0)
                sum += i;
    }
    cout<<"The sum of even numbers upto "<<n<<" is:"<<sum;

    return 0;
}

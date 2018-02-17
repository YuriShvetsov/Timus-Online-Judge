#include <iostream>
#include <stdlib.h>

using namespace std;

int a[20], n, _min=99999999;

int rec (int k1, int k2, int x)
{
    if (x == n)
    {
        if (_min > abs(k1-k2)) {
            _min = abs(k1-k2);
        }
    }
    else
    {
        rec (k1+a[x], k2, x+1);
        rec (k1, k2+a[x], x+1);
    }

    return 0;

}

int main ()
{
    int i;
    cin >> n;
    for (i = 0; i < n; i++)
        cin >> a[i];
    rec(0, 0, 0);
    cout << _min << endl;

    return 0;

}

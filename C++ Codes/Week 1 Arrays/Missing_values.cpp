//Time Complexity=O(n**2)
//Space Complexity=O(n)
#include <iostream>
using namespace std;

int missing_number(int a[],int n)
{
    int arr[9]={1,2,3,4,5,6,7,8,9};
    for(int i=0;i<9;i++)
    {
        int count=0;
        for(int j=0;j<n;j++)
        {
            if(arr[i]==a[j])
            {
                count+=1;
            }
        }
        if(count==0)
        {
            return arr[i];
        }
    }
    return -1;
}

int main()
{
    int a[]={1,2,3,9,8,6,5,4,11};
    int n=9;
    int i=missing_number(a,n);
    if(missing_number(a,n)!=-1)
    {
        cout<<i;
    }
    else{
        cout<<"No missing values.";
    }

    return 0;
}
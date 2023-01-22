#include <iostream>
using namespace std;
int find_min(int a[],int n)
{
    int min=0;
    for(int i=0;i<n;i++)
    {
        if(min>a[i] && a[i]>0 && a[i]!=0)
        {
            min=a[i];
        }
    }
    return min;
}
int* subtract(int a[],int n,int s)
{
    for(int j=0;j<n;j++)
    {
        a[j]-=s;
    }
    return a;
}
int kth_smallest(int a[],int n,int k)
{
    int min=find_min(a,n);
    int m=0;
    if(k==1)
    {
        return min;
    }
    while(k>0)
    {
        subtract(a,n,min);
        m+=min;
        cout<<min<<" ";
        min=find_min(a,n);
        k--;
    }
    min+=m;
    return min;
}

int main()
{
    int a[]={1,9,3,10};
    int n=4;
    int k=2;

    cout<<"\n"<<kth_smallest(a,n,k);
    return 0;
}
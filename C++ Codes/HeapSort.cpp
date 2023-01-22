#include <iostream>
using namespace std;
void swap(int *a,int *b)
{
    int t=*a;
    *a=*b;
    *b=t;
}
void heapify(int a[],int n,int i)
{
    int largest=i;
    int left=2*i+1;
    int right=2*i+2;

    if(left<n && a[left]>a[largest])
    {
        largest=left;
    }
    if(right<n && a[right]>a[largest])
    {
        largest=right;
    }
    if(largest!=i)
    {
        swap(&a[i],&a[largest]);
        heapify(a,n,largest);
    }
}
void HeapSort(int a[],int n)
{
    for(int i=n/2-1;i>=0;i--)
    {
        heapify(a,n,i);
    }
    for(int i=n-1;i>=0;i--)
    {
        swap(&a[0],&a[i]);
        heapify(a,i,0);
    }
}
void PrintArray(int a[],int n)
{
    int i;
    for(i=0;i<n;i++)
    {
        cout<<a[i]<<" ";
    }
    cout<<"\n";
}

int main()
{
    int n;
    cout<<"Enter size of the list::";
    cin>>n;
    int arr[n];
    cout<<"Enter the list::";
    for(int j=0;j<n;j++)
    {
        cin>>arr[j];
    }
    HeapSort(arr,n);
    cout<<"Sorted List:: ";
    PrintArray(arr,n);

    return 0;

}
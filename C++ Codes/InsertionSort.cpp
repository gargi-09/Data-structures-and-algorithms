#include <iostream>
using namespace std;

void InsertionSort(int a[],int n)
{
   int i, key, j;
    for (i = 1; i < n; i++)
    {
        key = a[i];
        j = i - 1;
 
       
        while (j >= 0 && a[j] > key)
        {
            a[j + 1] = a[j];
            j = j - 1;
        }
        a[j + 1] = key;
    }

}

int main()
{
    int n;
    cout<<"Enter size of list::";
    cin>>n;
    int arr[n];

    cout<<"Enter the list::";
    for(int j=0;j<n;j++)
    {
        cin>>arr[j];
    }
    InsertionSort(arr,n);
  for(int k=0;k<n;k++)
  {
      cout<<arr[k]<<" ";
  }

  return 0;
}
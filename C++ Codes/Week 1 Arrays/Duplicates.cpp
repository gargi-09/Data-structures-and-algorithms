//Time Complexity= O(n)
//Space Complexity=O(n)*

#include <iostream>
using namespace std;

int detect_duplicates(int a[],int n)
{
    int i=0;
    int j=n-1;
    int count=0;
    while(i<=n-2)
    {
        if(a[i]==a[j])
        {
            count+=1;
        }
        if(j==i+1){
            i++;
            j=n-1;
        }
        else{
            j--;
        }
    }
    return count;
}

int main()
{
    int a[]={1,2,3,1,4};
    int n=5;
    int c=detect_duplicates(a,n);
    if(detect_duplicates(a,n)!=0)
        {cout<<"Has duplicates "<<c;}
    else{
        cout<<"No duplicates";
    }
    return 0;

}
//DATA STRUCTURE IMPLEMENTATION
//ARRAYS
#include <iostream>

using namespace std;


int search_ele(int a[],int n,int ele);
int swap(int* a,int* b)
{
    int* temp=a;
    a=b;
    b=temp;
}
int* insert(int a[],int n,int pos,int ele)
{
    
        //Insert at beggining
        if(pos==n)
        {
            a[n]=ele;
            n++;
            return a;
        }
        for(int i=n-1;i>=pos;i--)
        {
            a[i]=a[i-1];
            
        }
        a[pos]=ele;
        
        return a;
    
}
int* deletion_by_pos(int a[],int n,int pos)
{
    
    if(pos==n-1){
        n--;
        return a;
    }
    n--;
    for(int i=pos;i<n;i++)
    {
        a[i]=a[i+1];
    }
    return a;
}
int* deletion_by_value(int a[],int n,int ele)
{
    int i=search_ele(a,n,ele);
    for(int j=i;j<n;j++)
    {
        a[j]=a[j+1];
    }
    return a;
}
int search_ele(int a[],int n,int ele)
{
    for(int i=0;i<n;i++)
    {
        if(a[i]==ele)
        {
            return i;
        }
    }
    return -1;
}
int* update_by_pos(int a[],int n,int pos,int ele)
{
    for(int i=0;i<n;i++)
    {
        if(i==pos)
        {
            a[i]=ele;
        }
    }
    return a;
}
int* update_by_value(int a[],int n,int oele,int nele)
{
    for(int i=0;i<n;i++)
    {
        if(a[i]==oele)
        {
            a[i]=nele;
        }
    }
    return a;
}
int* reverse(int a[],int n)
{
    for(int i=0;i<n/2;i++)
    {
        swap(a[i],a[n-1-i]);
    }
    return a;
}
void print_array(int a[],int n)
{
    for(int i=0;i<n;i++)
    {
        cout<<a[i]<<" ";
    }
    cout<<endl;
}

int main()
{
    int a[]={1,2,4,5};
    int n=4;
    int pos=2;
    update_by_value(a,n,4,3);
    print_array(a,n);
    if(search_ele(a,n,6)!=-1)
    {
        cout<<search_ele(a,n,6);
    }
    else{
        cout<<"Element not found"<<endl;
    }
    insert(a,n,4,0);
    n+=1;
    print_array(a,n);
    deletion_by_pos(a,n,4);
    n-=1;
    print_array(a,n);
    deletion_by_value(a,n,3);
    n-=1;
    print_array(a,n);
    int arr[4]={1,2,3,5};
    reverse(arr,4);
    print_array(arr,4);
    return 0;
}

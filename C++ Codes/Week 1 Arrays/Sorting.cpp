#include <iostream>
using namespace std;

void print_array(int a[],int n);
void swap_n(int*a,int*b)
{
    int temp;
    temp=*a;
    *a=*b;
    *b=temp;
}
int Max(int a[],int n)
{
    int max=a[0];
    for(int i=0;i<n;i++)
    {
        if(a[i]>max)
        {
            max=a[i];
        }
    }
    return max;
}
int*bubble_sort(int a[],int n)
{
    while(true)
    {
        int i=0;
        int j=1;
        bool swap=false;
        while(j<n)
        {
            if(a[i]>a[j])
            {
                swap_n(&a[i],&a[j]);
                swap=true;
            }
            i++;
            j++;
        }
        if(swap==false)
        {
            break;
        }
    }
    return a;
}
int*selection_sort(int a[],int n)
{
    int i=0;
    while(i<n)
    {
        int min=i;
        for(int j=i;j<n;j++)
        {
            if(a[min]>a[j])
            {
                min=j;
            }
        }
        if(min!=i)
        {
            swap_n(&a[min],&a[i]);
        }
        i++;
    }
    return a;
}
int*insertion_sort(int a[],int n)
{
    int key,j;
    for(int i=1;i<n;i++)
    {
        key=a[i];
        j=i-1;

        while(j>=0 && a[j]>key)
        {
            a[j+1]=a[j];
            j=j-1;
        }
        a[j+1]=key;
    }
    return a;
}
int partition(int a[],int low,int high)
{
    int x=a[high];
    int i=low-1;
    for(int j=low;j<=high-1;j++)
    {
        if(a[j]<x)
        {
            i++;
            swap_n(&a[i],&a[j]);
        }
    }
    swap_n(&a[i+1],&a[high]);
    return (i+1);
}
int*quick_sort(int a[],int low,int high)
{
    if(low<high)
    {
        int q=partition(a,low,high);
        quick_sort(a,low,q-1);
        quick_sort(a,q+1,high);
    }
    return a;
}
int partitionr(int a[],int low,int high)
{
    int rx=(rand()%high)+low;
    swap_n(&a[rx],&a[high]);

    return partition(a,low,high);
}
int*randomized_quick_sort(int a[],int low,int high)
{
    if(low<high)
    {
        int q=partitionr(a,low,high);
        randomized_quick_sort(a,low,q-1);
        randomized_quick_sort(a,q+1,high);
    }
    return a;
}
void merge(int a[],int low,int high,int mid)
{
    int n1=mid-low+1;
    int n2=high-mid;

    int sub1[n1];
    int sub2[n2];

    for(int i=0;i<n1;i++)
    {
        sub1[i]=a[low+i];
    }
    for(int j=0;j<n2;j++)
    {
        sub2[j]=a[mid+1+j];
    }

    int i=0,j=0,k=low;
    while(i<n1 && j<n2)
    {
        if(sub1[i]<=sub2[j])
        {
            a[k]=sub1[i];
            k++;
            i++;
        }
        else{
            a[k]=sub2[j];
            k++;
            j++;
        }
    }
    while(i<n1)
    {
        a[k]=sub1[i];
        i++;
        k++;
    }
    while(j<n2)
    {
        a[k]=sub2[j];
        j++;
        k++;
    }
}
void merge_sort(int a[],int low,int high)
{
    if(low>=high)
    {
        return;
    }
    
    int mid=low+(high-low)/2;
    merge_sort(a,low,mid);
    merge_sort(a,mid+1,high);
    merge(a,low,high,mid);
}
void count_sort(int a[],int n)
{
    int max=Max(a,n);
    int count_arr[max+1] {0};
    for(int i=0;i<n;i++)
    {
        
        count_arr[a[i]]+=1;
        
    }
    for(int i=1;i<max+1;i++)
    {
        count_arr[i]=count_arr[i]+count_arr[i-1];
    }
    int pos[n];
    for(int i=n-1;i>=0;i--)
    {
        pos[count_arr[a[i]]-1]=a[i];
        count_arr[a[i]]-=1;
    }
    for(int j=0;j<n;j++)
    {
        a[j]=pos[j];
    }
}
void counting_sort(int a[],int n,int exp)
{
    int max=Max(a,n);
    int count_arr[max+1] {0};
    for(int i=0;i<n;i++)
    {
        
        count_arr[(a[i]/exp)%10]+=1;
        
    }
    for(int i=1;i<max+1;i++)
    {
        count_arr[i]=count_arr[i]+count_arr[i-1];
    }
    int pos[n];
    for(int i=n-1;i>=0;i--)
    {
        pos[count_arr[(a[i]/exp)%10]-1]=a[i];
        count_arr[(a[i]/exp)%10]-=1;
    }
    for(int j=0;j<n;j++)
    {
        a[j]=pos[j];
    }
}
//Radix Sort

void radix_sort(int a[],int n)
{
    int m=Max(a,n);

    for(int exp=1;m/exp>0;exp*=10)
    {
        counting_sort(a,n,exp);
    }
}

//Dutch National Flag Sort

void dnf(int a[],int n)
{
    int low=0,mid=0,high=n-1;
    while(mid<=high)
    {
        if(a[mid]==0)
        {
            swap_n(&a[low],&a[mid]);
            low+=1;
            mid+=1;
        }
        else if(a[mid]==1)
        {
            mid+=1;
        }
        else if(a[mid]==2)
        {
            swap_n(&a[mid],&a[high]);
            high-=1;
        }
    }
    cout<<endl;
}

//Bucket Sort

void bucket_sort(int a[],int n);
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
    int n;
    cout<<"Enter the size of the array:";
    cin>>n;
    int a[n];
    cout<<"Enter the elements:";
    for(int i=0;i<n;i++)
    {
        cin>>a[i];
    }
    
      cout<<"Pick one:\n1.Bubble sort\n2.Selection sort\n3.Insertion sort\n4.Quick sort\n5.Randomized quick sort\n6.Merge sort\n7.Count sort\n8.Radix sort\n9.Dutch National flag problem\n-->";
        int ch=0;
        cin>>ch;
    
    

    switch (ch)
    {
        case 0:
        cout<<"Pick a valid value!"<<endl;
        break;
        case 1:
        bubble_sort(a,n);
        break;
        case 2:
        selection_sort(a,n);
        break;
        case 3:
        insertion_sort(a,n);
        break;
        case 4:
        quick_sort(a,0,n-1);
        break;
        case 5:
        randomized_quick_sort(a,0,n-1);
        break;
        case 6:
        merge_sort(a,0,n-1);
        break;
        case 7:
        count_sort(a,n);
        break;
        case 8:
        radix_sort(a,n);
        break;
        case 9:
        dnf(a,n);
        break;
        }
    
    print_array(a,n);
    
    return 0;
}
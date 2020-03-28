#include<stdio.h>
#include<conio.h>
voidmax_heapify(int a[], inti, int n);
voidbuild_maxheap(int a[],int n);
voidbuild_maxheap(int a[],int n )
{
	inti;
	for(i=(n/2);i>=0;i--)
	{
		max_heapify(a,i,n);
	}
}

voidmax_heapify(int a[],inti,int n)
{
	printf("\ni=%d",i);
	int largest=i;
	int left=2*i+1;
	int right=2*i+2;
	int temp;
	if(a[left]>a[i] && left<=n)
	{
		largest=left;
	}
	else
	largest=i;
	printf("\t left=%d",left);
	if(a[right]>a[largest] && right<=n)
	{
		largest=right;
	}
	printf("\t right=%d",right);
	if(i != largest)
	{
		temp=a[i];
		a[i]=a[largest];
		a[largest]=temp;
		max_heapify(a,largest,n);
	}
}

voidheapsort(int a[],int n)
{
	inti,temp;
	build_maxheap(a,n);
	for(i=n;i>=0;i--)
	{
		temp=a[0];
		a[0]=a[i];
		a[i]=temp;
		n=n-1;
		max_heapify(a,0,n);
	}
}
void main()
{
	clrscr();
	inti,n=5;
	int a[]={8,10,1,3,4};
	heapsort(a,4);
	printf("\nsorted elements are:\n");
	for(i=0;i<n;i++)
	{
		printf("%d",a[i]);
	}
	getch();
	}


#include<stdio.h>
#include<stdlib.h>
typedef struct poly
{
	int a;
	float b;
}poly;
int main()
{
	int K1,K2;
	int i=0,j=0;
	scanf("%d",&K1);
	poly A[11],B[11];
	for(i=0;i<K1;i++)
	{
		scanf("%d",&A[i].a);
		scanf("%f",&A[i].b);
	}
	scanf("%d",&K2);
	for(j=0;j<K2;j++)
	{
		scanf("%d",&B[j].a);
		scanf("%f",&B[j].b);
	}
	A[K1].a=-1;
	B[K2].a=-1;
	i=0;
	j=0;
	poly out[20];
	int n=0;
	while(i<K1||j<K2)
	{
		if(A[i].a>B[j].a)
		{
			out[n]=A[i];
			i++;
			//printf("1 ");
		}
		else if(A[i].a<B[j].a)
		{
			out[n]=B[j];
			j++;
			//printf("2 ");
		}
		else
		{
			out[n].a=A[i].a;
			out[n].b=A[i].b+B[j].b;
			i++;
			j++;
			//printf("3 ");
		}
		n++;
	}
	printf("%d",n);
	for(int s=0;s<n;s++)
	{
		if(out[s].b!=0)
			printf(" %d %.1f",out[s].a,out[s].b);
	}
}
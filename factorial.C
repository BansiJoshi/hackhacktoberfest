#include<conio.h>
#include<stdio.h>
void main()
{       int factorial(int);
	int fact,n;
	printf("Enter the number whose factorial has to be found");
	scanf("%d",&n);
	fact=factorial(n);
	printf("Factorial of %d is %d",n,fact);
	getch();
}
int factorial(int n)
{
	if(n==0 || n==1)
	return 1;
	else{
	n=n*factorial(n-1);
	}
	return n;
}

#include<stdio.h>
int main ()
{
	int a, m , n ;
	printf ("enter the no, position and no of bits");
	scanf("%d%d%d", &a, &m, &n);
	if(m>n){
		printf("%d", (a>>(m-n)) &(~(~0<<n)));
		}
	else{
	printf("invalid input");
	}	      
	return 0;
}

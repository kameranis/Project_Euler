/*
 * Largest Product in a grid
 * Konstantinos Ameranis
 */

#include <stdio.h>
#include <math.h>

int main() 
{
	freopen("a.in", "r", stdin);
	int prod=1, max=0, table[20][20];
	for(int i=0; i<20; i++)
		for(int j=0; j<20; j++)
			scanf("%d", &table[i][j]);
	for(int i=0; i<20; i++)
	{
		for(int j=0; j<17; j++)
		{
			prod=table[i][j]*table[i][j+1]*table[i][j+2]*table[i][j+3];
			if(prod>max) max=prod;
		}
	}
	for(int i=0; i<20; i++)
	{
		for(int j=0; j<17; j++)
		{
			prod=table[j][i]*table[j+1][i]*table[j+2][i]*table[j+3][i];
			if(prod>max) max=prod;
		}
	}
	for(int i=0; i<17; i++)
	{
		for(int j=0; j<17; j++)
		{
			prod=table[i][j]*table[i+1][j+1]*table[i+2][j+2]*table[i+3][j+3];
			if(prod>max) max=prod;
		}
	}
	for(int i=0; i<17; i++)
	{
		for(int j=3; j<20; j++)
		{
			prod=table[i][j]*table[i+1][j-1]*table[i+2][j-2]*table[i+3][j-3];
			if(prod>max) max=prod;
		}
	}
	printf("%d\n", max);
	return 0;
}


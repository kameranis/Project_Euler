/*
 * Largest Prime Factor
 * Computes the largest prime factor of argv[1]
 * Konstantinos Ameranis
 */

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <math.h>

int main(int argc, char *argv[]) {
	unsigned long long int N=atol(argv[1]), l= 775146;

	bool array[l+1];  
	for(unsigned long long int i=1; i<=l; i++) {  
		array[i]=true;  
	}  
	array[1]= false;  
	for(unsigned long long int i=2; i<=l; i++) {  
		if(array[i]==true) {
			for(unsigned long long int j=2; j*i<=l; j++) {  
				array[j*i]=false;  
			}  
		}  
	} 
	unsigned long long int i=l;
	while(!array[i] || (array[i] && N%i!=0)) i--;
	printf("%lld\n", i);
	return 0;
}

/*
 * Summation of Primes
 * Sums the first argv[1] primes
 * Konstantinos Ameranis
 */


#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <math.h>

int main(int argc, char *argv[]) 
{
    unsigned long int N=atol(argv[1]);
    unsigned long int sum=0;
    bool array[N+1];  
    for(unsigned long int i=1; i<=N; i++) 
    {
        array[i]=true;  
    }  
    array[1]= false;  
    for(unsigned long int i=2; i<=N; i++) 
    {  
        if(array[i]==true) 
        {
            sum+=i;
            for(unsigned long int j=2; j*i<=N; j++) 
            {  
                array[j*i]=false;  
            }  
        }  
    } 
    printf("%ld\n", sum);
    return 0;
}

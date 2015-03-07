/*
 * Multiples of 3 and 5
 * Computes the sum of all the multiples of 3 and 5 below 1000
 * Konstantinos Ameranis
 */

#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
int N=atoi(argv[1]);
int sum=0;
for(int i=1; i<N; i++) {
sum+= (i%3==0 || i%5==0) ? i : 0;
}
printf("%d\n", sum);
return 0;
}

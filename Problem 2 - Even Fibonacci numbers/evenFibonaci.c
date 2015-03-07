/*
 * Even Fibonacci numbers
 * Computes the sum of all the even fibonacci numbers below 4e6
 * Konstantinos Ameranis
 */

#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    int lim=atoi(argv[1]), sum=0, previous=1, current=2, next;
    while(current<=lim) {
        if(current%2==0) sum+=current;
        next=current+previous;
        previous=current;
        current=next;
    }
    printf("%d\n", sum);
    return 0;
}

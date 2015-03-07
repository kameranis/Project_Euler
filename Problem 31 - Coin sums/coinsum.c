/* Coin sums
 * Finds the possible ways to give 2 pounds
 * Konstantinos Ameranis 15.11.2013
*/
#include <stdio.h>

#define BALANCE 200 
#define int long int

int coins(int balance, int *values, int index);

int main() {
    int values[] = {200, 100, 50, 20, 10, 5, 2, 1};
    printf("%ld\n", coins(BALANCE, values, 0));
    return 0;
}

int coins(int balance, int *values, int index) {
    if(0==balance) return 1;
    if(balance < 0) return 0;
    int sum = 0;
    for(int i=index; i < 8; i++) {
        sum += coins(balance-values[i], values, i);
    }
    return sum;
}

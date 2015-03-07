/*
 * Lexicographic permutations
 * Prints the millionth lexicographic permutation of [0, 9]
 * Konstantinos Ameranis 10.9.2013
*/

#include <iostream>
#include <algorithm>

#define LIMIT 1000000

int main() 
{
    int myints[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
    int i;
    for(i=0; i<LIMIT-1; i++)
    {
        std::next_permutation(myints, myints+10);
    }
    for(i=0; i<10; i++) std::cout << myints[i];
    std::cout << '\n';
}

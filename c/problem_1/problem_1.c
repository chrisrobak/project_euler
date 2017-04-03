/*
 If we list all the natural numbers below 10 that are multiples of 3 or 5,
 we get 3, 5, 6 and 9. The sum of these multiples is 23.

 Find the sum of all the multiples of 3 or 5 below 1000.
*/
#include <stdlib.h>
#include <stdio.h>

int main(int argc, char *argv[]){
  if (argc != 2){
    printf("Require max number as arg to run\n");
    return 1;
  }
  int max_number = atoi(argv[1]);
  int answer = 0;
  for (int i=1; i<max_number; i++){
    if ((i % 3 == 0) || (i % 5 == 0)){
      answer += i;
    }
  }
  printf("Answer is: %i\n", answer);
  return 0;
}

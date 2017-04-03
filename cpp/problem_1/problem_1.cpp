/*
If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
*/
#include <iostream>


int main(int argc, char *argv[]){
  int answer = 0;
  if (argc != 2){
    std::cout << "Requires max number as argument to run" << std::endl;
    return 1;
  }
  int max_number = atoi(argv[1]);
  std::cout << "Processing for numbers under: " << max_number << std::endl;
  
  for (int i=1; i<max_number; i++){
    if ((i % 3 == 0) || (i % 5 == 0)){
      answer += i;
    }
  }
  std::cout << "The Answer Is: " << answer << std::endl;
  return 0;
}

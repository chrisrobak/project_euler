/*
  Each new term in the Fibonacci sequence is generated by adding
  the previous two terms. By starting with 1 and 2,
  the first 10 terms will be:
    1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
  By considering the terms in the Fibonacci sequence whose values
  do not exceed four million, find the sum of the even-valued terms.
 */

class Problem2 {
    public static void main(String[] args){
        if (args.length != 1){
            System.out.println("Require max number as argument to run");
        } else {
            int max_number = Integer.parseInt(args[0]);
            int answer = 0;
            int fib_value = 1;
            int current_number = 1;
            int previous_number = 1;
            while (fib_value < max_number){
                System.out.println("Current number: " + current_number);
                fib_value = current_number;
                if (fib_value >= max_number){
                    System.out.println("Anser is: " + answer);
                    break;
                }
                if (fib_value % 2 == 0){
                    answer += current_number;
                }
                current_number += previous_number;
                previous_number = current_number - previous_number;
            }
        }
    }
}

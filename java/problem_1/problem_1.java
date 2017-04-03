/*
 If we list all the natural numbers below 10 that are multiples of 3 or 5,
 we get 3, 5, 6 and 9. The sum of these multiples is 23.

 Find the sum of all the multiples of 3 or 5 below 1000.
 */

class Problem1 {
    public static void main(String[] args){
        if (args.length != 1){
            System.out.println("Require max number as argument to run");
        } else {
            int max_number = Integer.parseInt(args[0]);
            int answer = 0;
            for (int i=1; i<max_number; i++){
                if ((i % 3 == 0) || (i % 5 == 0)){
                    answer += i;
                }
            }
            System.out.println("Answer is: " + answer);
        }
    }
}

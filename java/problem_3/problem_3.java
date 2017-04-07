/*
 The prime factors of 13195 are 5, 7, 13 and 29.

 What is the largest prime factor of the number 600851475143 ?
 */
import java.util.*;

class Problem3 {
    public static void main(String[] args){
        if (args.length != 1){
            System.out.println("Require max number as argument to run");
        } else {
            long target_number = Long.parseLong(args[0]);
            ArrayList<Integer> known_primes = new ArrayList<Integer>();
            ArrayList<Integer> prime_factors = new ArrayList<Integer>();
            int current_number = 2;
            while (true){
                boolean is_prime = true;
                for (int prime_number : known_primes){
                    if (current_number % prime_number == 0){
                        is_prime = false;
                    }
                }
                if (is_prime){
                    known_primes.add(current_number);
                    if (target_number % current_number == 0){
                        prime_factors.add(current_number);
                        target_number = target_number / current_number;
                        for (int prime_number : known_primes){
                            if (target_number % prime_number == 0){
                                prime_factors.add(current_number);
                                target_number = target_number / prime_number;
                            }
                        }
                    }
                }
                current_number += 1;
                if (target_number == 1 || known_primes.contains(target_number)){
                    break;
                }
            }
            int answer = Collections.max(prime_factors);
            System.out.println("Max: " + answer);
        }
    };
}

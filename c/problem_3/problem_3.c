/*
 The prime factors of 13195 are 5, 7, 13 and 29.

 What is the largest prime factor of the number 600851475143 ?
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct node {
  long long data;
  struct node *next;
};

struct node* known_primes = NULL;  
struct node* prime_factors = NULL;

int is_prime(long long prime_to_check){
  printf("Checking is prime: %lu\n", prime_to_check);
  struct node *list_ptr = known_primes;
  if (!known_primes){
    return 1;
  }
  while(list_ptr){
    long long prime_mod_check = (prime_to_check % list_ptr->data);
    if (prime_mod_check == 0){
      return 0;
    };
    list_ptr = list_ptr->next;
  };
  printf("%lu is prime!", prime_to_check);
  return 1;
};

int is_in_list(struct node* list_to_check, long long number_to_check){
  struct node* list_ptr = list_to_check;
  if (!list_to_check){
    return 0;
  };
  while (list_ptr){
    if (list_ptr->data == number_to_check){
      return 1;
    }
    list_ptr = list_ptr->next;
  };
  return 0;
};

struct node *add_to_end_of_list(struct node *head, long long number_to_add){
  struct node *new_node = (struct node*)malloc(sizeof(struct node));
  new_node = malloc(sizeof(struct node));
  new_node->data = number_to_add;
  new_node->next = NULL;
  if (head != NULL){
    struct node* start = head;
    struct node* last = head;
    while (last->next != NULL){
      last = last->next;
    }
    last->next = new_node;
    return start;
  } else {
    head = new_node;
    return head;
  };
};

void print_list(struct node* head){
  printf("Printing list: \n");
  struct node* list_ptr = head;
  while (list_ptr){
    printf("Factor: %i\n", list_ptr->data);
    list_ptr = list_ptr->next;
  }
};

long long max_number_in_list(struct node* head){
  long long max_number = 0;
  struct node* list_ptr = head;
  while (list_ptr){
    if (list_ptr->data > max_number){
      max_number = list_ptr->data;
    }
    list_ptr = list_ptr->next;
  };
  return max_number;
};

int main(int argc, char *argv[]){
  if (argc != 2){
    printf("max number is required as argument to script\n");
    return 1;
  }
  long long target_number = strtoull(argv[1], NULL, 10);
  long long current_number = 3;
  known_primes = add_to_end_of_list(known_primes, 2);
  while (1){
    int current_is_prime = is_prime(current_number);
    if (current_is_prime){
      known_primes = add_to_end_of_list(known_primes, current_number);
      long long target_mod_num = target_number % current_number;
      if (target_mod_num == 0){
        printf("%lu mod %lu == %lu", target_number, current_number, target_mod_num);
        prime_factors = add_to_end_of_list(prime_factors, current_number);
        target_number = target_number / current_number;
        struct node* list_ptr = known_primes;
        while (list_ptr != NULL){
          if (target_number % list_ptr->data == 0){
            prime_factors = add_to_end_of_list(prime_factors, list_ptr->data);
            target_number = target_number / list_ptr->data;
          }
          list_ptr = list_ptr->next;
        };
        print_list(prime_factors);
      };
    };
    int is_in_primes = is_in_list(known_primes, target_number);
    if (target_number == 1 || is_in_primes){
      break;
    };
    current_number = current_number + 2;
  };
  printf("Prime Numbers:\n");
  print_list(known_primes);
  printf("Prime Factors:\n");
  print_list(prime_factors);
  long long largest_prime_factor = max_number_in_list(prime_factors);
  printf("largest prime factor: %lu\n", largest_prime_factor);
};

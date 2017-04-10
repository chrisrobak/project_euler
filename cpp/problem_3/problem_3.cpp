/*
 The prime factors of 13195 are 5, 7, 13 and 29.

 What is the largest prime factor of the number 600851475143 ?
*/
#include <iostream>

struct node {
  long data;
  node *next;
};

bool is_prime(node* known_primes, long prime_to_check){
  node *list_ptr = known_primes;
  if (!known_primes){
    return true;
  }
  while(list_ptr != nullptr){
    long prime_mod_check = (prime_to_check % list_ptr->data);
    if (prime_mod_check == 0){
      return false;
    };
    list_ptr = list_ptr->next;
  };
  return true;
};

bool is_in_list(node* list_to_check, long number_to_check){
  node* list_ptr = list_to_check;
  if (!list_to_check){
    return false;
  }
  while (list_ptr != nullptr){
    if (list_ptr->data == number_to_check){
      return true;
    };
    list_ptr = list_ptr->next;
  };
  return false;
};

void add_to_end_of_list(node* &head, long number_to_add){
  node* new_node = new node;
  new_node->data = number_to_add;
  new_node->next = nullptr;
  if (!head){
    head = new_node;
    return;
  } else {
    node* last = head;
    while (last->next != nullptr) last=last->next;
    last->next = new_node;
  }
};

void print_list(node* head){
  node* list_ptr = head;
  while (list_ptr!=nullptr){
    std::cout << list_ptr->data << std::endl;
    list_ptr = list_ptr->next;
  };
};

int main(int argc, char *argv[]){
  if (argc != 2){
    std::cout << "Require max number as argument to script" << std::endl;
    return 1;
  }
  long target_number = atol(argv[1]);
  long current_number = 2;
  node* known_primes = NULL;
  node* prime_factors = NULL;
  
  while(true){
    bool current_is_prime = is_prime(known_primes, current_number);
    if (current_is_prime){
      add_to_end_of_list(known_primes, current_number);
      if (target_number % current_number == 0){
        add_to_end_of_list(prime_factors, current_number);
        target_number = target_number / current_number;
        node* list_ptr = known_primes;
        while (list_ptr != nullptr){
          if (target_number % list_ptr->data == 0){
            add_to_end_of_list(prime_factors, list_ptr->data);
            target_number = target_number / list_ptr->data;
          };
          list_ptr = list_ptr->next;
        };
      };
    };
    bool is_in_primes = is_in_list(known_primes, target_number);
    if (target_number == 1 || is_in_primes){
      break;
    };
    current_number = current_number + 1;
  };
  print_list(prime_factors);
}

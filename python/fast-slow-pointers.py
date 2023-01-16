#!/usr/bin/env python

## Original Solution (Recursive method)
def is_happy_number(n):
    def down_to_single_digit(n):
        n = sum([i ** 2 for i in list(map(int, str(n)))])
        while n > 9:
            n = sum([i ** 2 for i in list(map(int, str(n)))])
            if n > 9:
                down_to_single_digit(n)
            else:
                return n
    return n

    return True if down_to_single_digit(n) == 1 else False

  
## Original Solution to detemine the linked list is cyclic   
def detect_cycle(head):
   sp = head
   fp = head
   
   while sp != fp:
      sp = head.next
      fp = head.next.next

      print(sp, fp)
      if sp == fp:
         return True
      elif fp.next is None:
         return False
   return False

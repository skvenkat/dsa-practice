#!/usr/bin/env python

def is_palindrome(s):
  lp, rp = 0, (len(s) - 1)

  while lp<=rp:
    if s[lp] == s[rp]:
      lp += 1
      rp -= 1
    else:
      return False

  return True


def find_sum_of_three(nums, target):
   # using inbuilt sort function
   nums.sort()
   n = len(nums)
   for i in range(n-1):
      lsb = i+1
      msb = (n - 1)
      while lsb < msb:
         sum_of_3 = (nums[i] + nums[lsb] + nums[msb])
         if sum_of_3 == target:
            return True
         elif sum_of_3 > target:
            msb -= 1
         else:
            lsb += 1
   return False


def is_palindrome_after_one_mismatch(s):
    left = 0
    right = len(s) - 1
    mismatch = 0
    while left <= right:
      if s[left] == s[right]:
          left += 1
          right -= 1
      else:
          if s[left + 1] == s[right]:
              left += 2
              right -= 1
              mismatch += 1
          elif s[left] == s[right - 1]:
              left += 1
              right -= 2
              mismatch += 1
          else:
              return False

    # check the mismatch greater than 1 to confirm its a valid palindorme
    if mismatch < 2:
        return True
    return False

## Original Solution
# Dependency for is_happy_number() method
def down_to_single_digit(n):
    n = sum([i ** 2 for i in list(map(int, str(n)))])
    while n > 9:
        n = sum([i ** 2 for i in list(map(int, str(n)))])
        if n > 9:
            down_to_single_digit(n)
        else:
            return n
    return n

def is_happy_number(n):
    return True if down_to_single_digit(n) == 1 else False

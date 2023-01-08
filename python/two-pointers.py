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

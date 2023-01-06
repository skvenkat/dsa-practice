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

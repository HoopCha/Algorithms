#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  #Possible Options
  rps = ['rock', 'paper', 'scissors']
  #Base Cases
  if n == 0:
    return [[]]
  elif n == 1:
    return [[choice] for choice in rps]
  #Recursion
  else:
    return [[choice] + x for choice in rps for x in rock_paper_scissors(n-1)]

print(len(rock_paper_scissors(2)))

# if __name__ == "__main__":
#   if len(sys.argv) > 1:
#     num_plays = int(sys.argv[1])
#     print(rock_paper_scissors(num_plays))
#   else:
#     print('Usage: rps.py [num_plays]')
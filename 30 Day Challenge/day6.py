'''
Let's Review!
'''
#!/bin/python

import sys

n = int(input().strip())

for x in range(n,0,-1):
    print(' ' * (x-1) + '#' * (n-x+1) )


'''
 6

     #
    ##
   ###
  ####
 #####
######

'''
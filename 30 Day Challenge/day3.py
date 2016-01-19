'''
If-Else Statements!
'''
__author__ = 'shbaek'
#!/bin/python

import sys


N = int(input().strip())
'''
    If N is odd, print "Weird".
    If N is even and, in between the range of 2 and 5(inclusive), print "Not Weird".
    If N is even and, in between the range of 6 and 20(inclusive), print "Weird".
    If N is even and N>20, print "Not Weird".
'''
# Constraint 1<=N<=100
if 1<=N<=100:
    if N%2==0 :
        if 2<=N<=5:
            print("Not Weird")
        elif 6<=N<=20:
            print("Weird")
        elif N>20:
            print("Not Weird")
    else:
        print("Weird")
else:
    print("Alert Constraint!!!")




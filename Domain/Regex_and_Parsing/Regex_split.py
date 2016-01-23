import re

print("\n".join(x for x in re.split('[,.]*', input())).strip())

'''
Sample Input

100,000,000.000

Sample Output

100
000
000
000
'''

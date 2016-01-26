import re

for _ in range(int(input())):
    m = re.findall(r'(?<!^)#[0-9a-f]{3,6}', input().strip(), flags=re.I)
    if m:
        print('\n'.join(m))

'''

Specifications of HEX Color Code
■ It must start with a '#' symbol.
■ It can have 3 or 6 digits.
■ Each digit is in the range of 0 to F. (i.e. 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, A, B, C, D, E and F).
■ A-F letters can be in lower case too. (i.e. a, b, c, d, e and f are also valid digits).

r'(?<!^)#[0-9a-f]{3,6}'
Pattern
r'^#([a-f0-9]{3,6})$'



Sample Input

11
#BED
{
    color: #FfFdF8; background-color:#aef;
    font-size: 123px;
    background: -webkit-linear-gradient(top, #f9f9f9, #fff);
}
#Cab
{
    background-color: #ABC;
    border: 2px dashed #fff;
}

Sample Output

#FfFdF8
#aef
#f9f9f9
#fff
#ABC
#fff

'''

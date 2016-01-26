import re

result = []
for _ in range(int(input())):
    email = input()
    if re.search(r'^\w+\s<[a-z]{1}[\w.-]*@[a-z]+.\w{1,3}>', email, re.IGNORECASE):
        result.append(email)

for x in result:
    print(x)
'''
Sample Input

2
DEXTER <dexter@hotmail.com>
VIRUS <virus!@variable.:p>

Sample Output

DEXTER <dexter@hotmail.com>

mine : r'^\w+\s<([a-z]+[\w\d.-])@([\da-z]+)\.([a-z]{1,3})>$'

r'^\w+\s<[a-zA-Z]{1}[\w.-]*@[a-zA-Z]+.\w{1,3}>'

A valid email address follows the rules below:
- Email must have three basic components: username @ website name . extension.
- The username can contain: alphanumeric characters, -,. and _.
- The username must start with an English alphabet character.
- The website name contains only English alphabet characters.
- The extension contains only English alphabet characters, and its length can be 1, 2, or 3.
'''

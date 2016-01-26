import re

result = []
for _ in range(int(input())):
    email = input()
    if re.search(r'^([a-z0-9_-]+)@([\da-z]+)\.([a-z]{1,3})$', email, re.IGNORECASE):
        result.append(email)

print(sorted(result))

'''
3
lara@hackerrank.com
brian-23@hackerrank.com
britts_54@hackerrank.com

/^([a-z0-9_-]+)@([\da-z]+)\.([a-z]{1,3})$/
Username can only contain letters, digits, dash and underscore.

Website name can have letters and digits.

Maximum length of the extension is 3.
'''

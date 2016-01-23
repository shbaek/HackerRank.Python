import re

N = input().strip()
result = list()
for _ in range(int(N)):
    M = input().strip()
    result.append(bool(re.match(r'^[+-]?\d*.\d+$', M)))
for x in result:
    print(x)

('\n'
 'regex = r\'^[+-]?\d*.\d+$\'\n'
 '* - 0번 이상 반복\n'
 '+ - 1번 이상 반복\n'
 '\n'
 '^ - 입력값 시작\n'
 '^[+-] - + 또는 - 로 시작\n'
 '\n'
 '\b - 문자와 공백 사이에 문자를 찾음\n'
 '\B - 문자와 공백 사이가 아닌 값을 찾음\n'
 '\d - 숫자를 찾음\n'
 '\D - 숫자가 아닌 값 찾음\n'
 '\s - 공백 문자 찾음\n'
 '\S - 공백 문자가 아닌 문자 찾음\n'
 '\n'
 '\n'
 '$ - 입력값 끝\n'
 '\n'
 '\n'
 '\n'
 'Sample Input\n'
 '\n'
 '4\n'
 '4.0O0\n'
 '-1.00\n'
 '+4.54\n'
 'SomeRandomStuff\n'
 '\n'
 'Sample Output\n'
 '\n'
 'False\n'
 'True\n'
 'True\n'
 'False\n'
 '\n')

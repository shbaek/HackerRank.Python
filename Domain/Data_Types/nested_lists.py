'''
5
[['Harry','37.21'],['Berry','37.21'],['Tina','37.2'],['Akriti','41'],['Harsh','39']]
a_list = [['Harry','37.21'],['Berry','37.21'],['Tina','37.2'],['Akriti','41'],['Harsh','39']]
'''
a_list = []
for _ in range(0, int(input())):
    a_list.append([input(), float(input())])

second_largest = sorted(list(set([score for name, score in a_list])))[1]

print('\n'.join([name for name, score in sorted(a_list) if score == second_largest]))

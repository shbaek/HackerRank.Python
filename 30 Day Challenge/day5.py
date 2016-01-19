'''
Loops!
'''
__author__ = 'shbaek'


def sigma(a, b, frm, to):
    result = 0
    for u in range(frm, to+1):
        result += (pow(2,u)*b)
        print(a + result),
    return result

T=int(input())

for i in range(0,T):
    tmp = input().split(' ')
    a = int(tmp[0])
    b = int(tmp[1])
    N = int(tmp[2])
    sigma(a, b, 0, N-1)
    print('')

'''
2
5 3 5
0 2 10

Sample Output
In the first case: a=5, b=3 ,N=5
1st term =   5+(pow(2,0)*3)=8
2nd term = 5+(pow(2,0)*3)+(pow(2,1)*3)=14
3rd term =  5+(pow(2,0)*3)+(pow(2,1)*3)+(pow(2,2)*3)=26
4th term =  5+(pow(2,0)*3)+(pow(2,1)*3)+(pow(2,2)*3)+(pow(2,3)*3)=50
5th term =  5+(pow(2,0)*3)+(pow(2,1)*3)+(pow(2,2)*3)+(pow(2,3)*3)+(pow(2,4)*3)=98

8 14 26 50 98
2 6 14 30 62 126 254 510 1022 2046
'''
class Calculator():
    @staticmethod
    def power(n, p):
        if n < 0 or p < 0:
            raise Exception('n and p should be non-negative')
        else:
            return pow(n, p)


myCalculator = Calculator()
for i in range(int(input())):
    n, p = map(int, input().split())
    try:
        ans = myCalculator.power(n, p)
        print(ans)
    except Exception as e:
        print(e)

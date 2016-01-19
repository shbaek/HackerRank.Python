'''
Logical Operators + Class vs. Instance!
'''
class Person:
    age = 0
    def __init__(self, initial_Age):
        # Add some more code to run some checks on initial_Age
        if initial_Age < 0:
            print("This person is not valid, setting age to 0.")
            self.age = 0
        else:
            self.age = initial_Age
    def amIOld(self):
        # Do some computations in here and print out the correct statement to the console
        if self.age < 13:
            print("You are young.")
        elif 13 <= self.age < 18:
            print("You are a teenager.")
        else:
            print("You are old.")

    def yearPasses(self):
        # Increment the age of the person in here
        self.age += 1


T=int(input())
for i in range(0,T):
    age=int(input())
    p=Person(age)
    p.amIOld()
    for j in range(0,3):
        p.yearPasses();
    p.amIOld();
    print ("")

'''
 4
-1
10
16
18

-- For the first testcase, the age is less than 0 so we set the age to 0.Three years pass and the age is 3. So we print out:
This person is not valid, setting age to 0.
You are young.
You are young.

--For the second testcase, the age is 10, which is considered young according to our program. Three years pass and the age is 13. 13 is considered a 'teenager' age so we print out:
You are young.
You are a teenager.

--For the third testcase, the age is 16, which is the age of a teenager. Three years pass and the age is 19. 19 is considered an 'old' age according to our program so we print out:
You are a teenager.
You are old.

For the last testcase, the age is 18, which is considered an old age according to our program. Three years pass and the age is 21. 21 is still considered old so we print out:
You are old.
You are old.













'''
import math;

a = 5
b = 6
c = 2
d = 1

# Oppgave 1
print(a + b + d)

# Oppgave 2
x = a * b - c
print(x)

# Oppgave 3
z = 'spicy food'

if z =='spicy food':
    print('I love it!')
else:
    print("I don't like it")

# Oppgave 4
year = ('january', 'february', 'mars', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december')
for w in year:
    print(w)

# oppgave 5
prime_tall = [1, 3, 2, 5, 8, 49, 0, 15, 212, 13, 176, 21, 7, 29, 20, 14]

def splitevenodd (A):
    evenlist = []
    oddlist = []
    for i in A:
        if (i % 2 == 0):
            evenlist.append(i)
        else:
            oddlist.append(i)
    print("Even lists:", evenlist)
    print("Odd lists:", oddlist)

A = prime_tall
splitevenodd(A)
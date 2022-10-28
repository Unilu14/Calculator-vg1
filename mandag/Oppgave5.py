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
#######lkd####################
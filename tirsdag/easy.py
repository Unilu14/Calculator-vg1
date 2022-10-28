from matplotlib import pyplot as plt
import numpy as np 

word1 = 2
word2 = 4
word3 = 6
word4 = -2
word5 = 10

# Oppgave 1
x = [word1, word2, word3, word4, word5]
print("Number list", x)

i = word1 + word2 + word3 + word4 + word5
print("The answer is:", i)

# Oppgave 2
numbers = [word1, word2, word3, word4, word5]
list.sort(numbers)
print("Numbers in order:", numbers)

# Oppgave 3
countries  = ["Nicaragua", "Cuba", "Kina", "Østerrike", "Nederland", "Norge", "Chile", "Brasil","Venezuela"]
konsumprisindeks = [3.4, 1.2, 3.7, 5.3, 4.9, 6.9, 8.1, 7.2, 3.4 ]
colors = [ "yellow", "red", "blue", "silver", "deeppink", "brown", "grey", "cyan", "darksalmon"]

y = np.array(konsumprisindeks)

plt.pie(y, labels = countries, colors = colors)
plt.show()

# Oppgave 4
sum = 0
t = 1
while t < 51:
    print(t)
    t += 1
    sum += t
print("Numbers from 1 to 50 added is:", sum)

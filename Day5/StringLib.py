import random
import string

x = random.randint(1000, 9999)
print(x)

std = ["Tom", "Jack", "Jerry", "Mahi", "Ruby"]
print(random.choice(std))

name = "abcde"
print(random.choice(name))

x = ''.join(random.choice(string.ascii_lowercase) for i in range(5))
print(x)

y = ''.join(random.choices(string.ascii_lowercase, k=5))
print(y)

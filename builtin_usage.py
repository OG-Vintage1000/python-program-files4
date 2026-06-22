import math
import random
import platform

ran = random.randint(1, 100)
print("Let's find a random number between 1 and 100.")
print(ran)
print()

print("Let's round down the square root of our newly acquired random number to the lowest integer value.")
val = math.sqrt(ran)
num = math.floor(val)
print(num)
print()

print(dir(platform))
print()
print(f"The operating system is {platform.system()} and the current Python version is {platform.python_version()}.")

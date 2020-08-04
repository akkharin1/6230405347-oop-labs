import random
import math

first_num = random.randint(1,10)
second_num = random.randint(1,10)
average = (first_num + second_num) / 2
standard_deviation = math.sqrt(((first_num - average)**2)+(first_num - average)**2) / 2
print("first_num is: ",first_num)
print("second_num is: ",second_num)
print("avarage is: ",average)
print("standard deviation is: ",standard_deviation)
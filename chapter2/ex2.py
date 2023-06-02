from math import sqrt
import numpy

numbs = [512, 516, 518, 516, 515, 513, 516, 515, 512, 517]
total = sum(numbs)
#print(total)
#counter
k = 0
for value in numbs:
    k += 1
#mean 
mean = total / k
print(f"the mean is: {mean}")

#median
if k%2 == 0:
    median =  (numbs[int((k/2)-2)] + numbs[int(k/2)]) / 2
    print(numbs[int((k/2)-2)])
    print(numbs[int(k/2)])
else:
    middleIndex = (len(numbs) - 1)/2
    print(middleIndex)
    median = numbs[middleIndex]
print(f"the median is: {median}")

#standart deviation 
sd_sum = 0
for value in numbs:
    dif = mean - value
    sd_sum = sd_sum + (dif**2)

print(sd_sum)
variation = sd_sum / (k -1)
stand_deviation = round(sqrt(variation),4)
print(f"standart deviation is: {stand_deviation}")

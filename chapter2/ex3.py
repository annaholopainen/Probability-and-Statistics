
from math import sqrt
import numpy as np
import matplotlib.pyplot as plt
import matplotx
 
# creating the dataset
data = {'5':8, '6':10,
        '7':30, '8':36, '9':39, '10':29}
courses = list(data.keys())
values = list(data.values())


# getting the mean
total_students = 0
sumgrades = 0
for key, value in data.items():
    #print(key)
    #print(value)
    total_students = total_students + value
    sumgrades = sumgrades + (int(key)*value)

#print(sumgrades)
#print(total_students)

mean = sumgrades / (total_students - 1)

# getting the standart deviation 
sd_sum = 0
for value in data:
    #print(data[value])
    #print(value)
    dif = mean - int(value)
    sd_sum = sd_sum + (dif**2)*int(data[value]) 

#print(sd_sum)
variation = sd_sum / (total_students - 1)
standart_deviation = sqrt(variation)

fig = plt.figure(figsize = (10, 5))
 
# creating the bar plot
plt.bar(courses, values, color ='maroon',
        width = 0.4)
plt.axhline(y=mean,linewidth= 3, color='black',label = f"mean= {round(mean,3)}" )
plt.axhline(y=standart_deviation,linewidth= 3, color='pink',label = f"standart deviation= {round(standart_deviation, 3)}" )
plt.legend() 
plt.xlabel("Grades")
plt.ylabel("No. of students")
plt.title("French final exam grades from 1991 highschool students")
plt.show()
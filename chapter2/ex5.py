from math import sqrt


data =  {"7":7, "6":20, "5":30,  "4":16, "3":9, "2":4}
# data {Grade in numbers: Amount}
# finding the mean
# counter 
k = 0
total = 0
totalamount = 0
for key, value in data.items():
    k += 1
    total = total + int(key)*value
    totalamount = totalamount + value

mean = round(total / totalamount, 2)
print(f"mean is: {mean}")

# finding the standart deviation 
sd_sum = 0
for grade in data:
    dif = mean - int(grade)
    sd_sum = sd_sum + (dif**2)*data[grade]

variation = sd_sum / (totalamount - 1)
sd = sqrt(variation)

print(f"standart deviation is: {round(sd, 2)}")
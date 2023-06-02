fib = [1,1,2,3,5,8,13,21,34,55]
#counter 
k = 0
# sum of values 
total = 0
for value in fib:
    total = total + value
    k+= 1

mean = total / k
print(mean)


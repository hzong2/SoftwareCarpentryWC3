# Add all the even numbers between 1 and 100

#Initialize the sum
num = 1
finalnum = 100
sum = 0

while num <= finalnum:
    if (num % 2 ==0):
         sum = sum + num
    num = num+1

print(sum)
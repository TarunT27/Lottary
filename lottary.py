import random

lottery_number = []

for i in range(7):
    lottery_number.append(random.randint(0,9))

print("The lottery number is: ")
for num in lottery_number:
    print(num, end='')
print() 

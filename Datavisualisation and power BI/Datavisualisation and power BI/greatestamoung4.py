numbers=[]
for i in range(4):
    number=int(input(f"enter your number{i+1}" ))
    numbers.append(number)
    
max_num=numbers[0]

for number in numbers:
    if(number>=max_num):
        max_num=number
print("the greatest number is: ", max_num )
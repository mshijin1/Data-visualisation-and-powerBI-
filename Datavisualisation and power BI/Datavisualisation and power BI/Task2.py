from prettytable import PrettyTable
list=[
    ["stdid","stdname","standard","Age","Hindi","English","Maths","Science","Computer","Total"],
["std101","Ashish,Kumar","10th",15,67,89,87,89,90,422],
["std102","Abhishek Kumar","10th",14,85,45,48,90,45,313],
["std103","Aman","10th",15,23,56,78,78,67,302],
["std104","Rahul","10th",14,45,67,45,45,56,258],
["std105","Ruby","10th",13,89,67,89,93,65,403],
["std106","Suman","10th",13,90,46,67,67,67,337],
["std107","Saurabh","10th",15,45,23,34,45,34,181],
["std108","Sumit","10th",14,23,45,67,78,90,303],
["std109","kamlesh","10th",15,45,56,78,99,67,345],
["std110","Rohan","10th",15,34,12,24,45,56,171],
]

table = PrettyTable()

# Use the first row as the header
table.field_names = list[0]

# Add the rest of the rows to the table
for row in list[1:]:
    table.add_row(row)

print(table)

#Display names of students whose marks in english are greater than 50
print("#Display names of students whose marks in english are greater than 50")
for row in range(1,len(list)):
    if(list[row][5]>50):
        print(list[row][1])
        
#Display Student name and age of top fur scorer in math
print("-------------------------------------------------------------------------------")
print("#Display Student name and age of top fur scorer in math")
# max=[]
# for row in range(1,len(list)):
#     for i in range(4):
#         if(list[row][5]>max)
        
maths_index = list[0].index("Maths")

# Sort the data based on Maths marks in descending order
sorted_list = [list[0]] + sorted(list[1:], key=lambda x: x[maths_index], reverse=True)

for i in range(1,5):
    print(sorted_list[i][1],sorted_list[i][3],sorted_list[i][6])
    
print("------------------------------------------------------------------------------")
print("#Display name, Id, age of students who are bottom three scorer in computer.")
computer_index=list[0].index("Computer")
#Sort the data based on computer in acsending order
sorted_list2=[list[0]]+sorted(list[1:],key=lambda x: x[computer_index])

for i in range(1,4):
    print(sorted_list2[i][0],sorted_list2[i][1],sorted_list2[i][3])  


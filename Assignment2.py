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

# keys=['stdid','stdname','standard','Age','Hindi','English','Maths','Science','Computer','Total']
# values=[["std101","Ashish,Kumar","10th",15,67,89,87,89,90,422],
#  ["std102","Abhishek Kumar","10th",14,85,45,48,90,45,313],
#  ["std103","Aman","10th",15,23,56,78,78,67,302],
#  ["std104","Rahul","10th",14,45,67,45,45,56,258],
#  ["std105","Ruby","10th",13,89,67,89,93,65,403],
#  ["std106","Suman","10th",13,90,46,67,67,67,337],
#  ["std107","Saurabh","10th",15,45,23,34,45,34,181],
#  ["std108","Sumit","10th",14,23,45,67,78,90,303],
#  ["std109","kamlesh","10th",15,45,56,78,99,67,345],
#  ["std110","Rohan","10th",15,34,12,24,45,56,171],]




# print the data in table formate
table=PrettyTable()
table.field_names=list[0]
for row in list[1:]:
    table.add_row(row)
print(table)

#1.Display names of students whose marks in english are greater than 50
print("-------------------------------------------------------------------------------------------------------------------------------------------")
print("1.Display names of students whose marks in english are greater than 50")
header=list[0] #field name of the list of lists
students_dict={}

for students in list[1:]:
    student_dict={header[i]:students[i] for i in range(len(header))}           #creating a Dictionary with Field names and its coresponding students details 
    students_dict[students[0]]=student_dict

Marks_above50=[]  #creating a list of students whose marks in english is more than 50

for student in students_dict.values():
    if(student["English"]>50):
        Marks_above50.append(student["stdname"])
print("students having marks above 50:", Marks_above50)

print("-------------------------------------------------------------------------------------------------------------------------------------------")
print("Display students name and age of top 4 scorers in Maths")

Top_4_scorers=sorted(students_dict.values(),key=lambda x:x["Maths"],reverse=True)[:4] #sorting student dictionary in decending Order 
for student in Top_4_scorers:
    print(student["stdname"], student["Age"])
    
print("------------------------------------------------------------------------------------------------------------------------------------")
print("Display names,Id,Age of students who are bottom 3 scorers in computer Science")

bottom_3_scorers=sorted(students_dict.values(),key=lambda x:x["Computer"])[:3] #sorting student dictionary in ascending Order
for student in bottom_3_scorers:
    print("name:",   student["stdname"], "ID:",   student["stdid"], "Age:",   student["Age"])
    
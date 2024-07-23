# # Write a python program to handle a zero division error.
# print("Write a python program to handle a zero division error.")
# print("Shijin")
# print("is")
# print("a")
# try:
#     a=100/0
# except ZeroDivisionError as err:
#     print(err)
# print("good")
# print("boy")

# print("--------------------------------------------------------------------------------------------------------------------------------------------")
# #Write a pyhon program that prompts the user to input an integer and raises a valueError exception if the input is not a valid integer
# print("Write a pyhon program that prompts the user to input an integer and raises a valueError exception if the input is not a valid integer")
# try:
#     userInpur= int(input("enter an integer value"))
# except ValueError:
#     print("this is not an integer value") 


print("--------------------------------------------------------------------------------------------------------------------------------------------")
#Write a python program that opens a file and handles a FileNotFoundError exception if the file does not exist
print("Write a python program that opens a file and handles a FileNotFoundError exception if the file does not exist")
path="sampletextfiles.txt\intro.txt"
try:
    with open(path) as file:
        content=file.read()
        print(content)
except FileExistsError:
    print("file does not exist")
    
print("--------------------------------------------------------------------------------------------------------------------------------------------")
print("Write a python program that prompts the user to input two numbers and raises a TypError Exception if the inputs are not numerical ")
try:
    input1=float(input("Enter your first number"))
    input2=float(input("Enter your second number"))
except TypeError:
    print("Error: Type error occured")
except ValueError:
    print("Error: Please enter a valid number")
print("Numbers entered:",input1,"and",input2)

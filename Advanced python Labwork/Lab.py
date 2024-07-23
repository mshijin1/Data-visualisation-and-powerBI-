print("Write a function in python to read the content from a text file 'ABC.txt' line by line and display the same on the screen.")

path='Labwork\Exciting.txt'
def read_content(path):
    try:
        with open(path,'r') as file:
            content=file.read()
            for line in content:
                print(line,end=" ")
                
    except FileNotFoundError:
        print(f"The file at {path} was not found.")
    except IOError:
        print(f"An error occurred while reading the file at {path}.")
              
     
     
     
     
     
     
     
     
     
     
     
    #      with open(Exciting.txt, 'r') as file:
    #      content=file.read()
    # for line in content:
    #     print(line,end=" ")
    
print("--------------------------------------------------------------------------")
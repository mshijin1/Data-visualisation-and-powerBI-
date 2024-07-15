second=int(input("Enter time in number"))

#time validation

if(second>=0):
    hour=0
    min=0
    if(second>=3600):
        hour=second/3600
        second=second%3600
    if(second>=60):
        min=second/60
        second=second%60
    
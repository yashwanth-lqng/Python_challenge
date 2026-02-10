n=int(input("Enter the number of marks: "))
marks=[0]*n
valid_students=0
failed_students=0
for i in range(n):
    marks[i]=int(input("Enter mark "+str(i+1)+": "))

print("\nMarks and their corresponding grades:")

for i in marks:
    if i>=90 and i<=100:
        print(str(i)+" --> Excellent")
        valid_students+=1
    elif i>=75 and i<90:
        print(str(i)+" --> Very Good")
        valid_students+=1
    elif i>=60 and i<75:
        print(str(i)+" --> Good")
        valid_students+=1
    elif i>=40 and i<60:
        print(str(i)+" --> Average")
        valid_students+=1
    elif i>=0 and i<40:
        print(str(i)+" --> Fail")
        failed_students+=1
        valid_students+=1
    else:
        print(str(i)+" --> Invalid")

print("Total Valid students: "+str(valid_students))
print("Total Failed students: "+str(failed_students))
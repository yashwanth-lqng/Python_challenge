name=input("Enter your name:")
mail=input("Enter your email id:")
mobile=input("Enter your mobile number:")
age=int(input("Enter your age:"))
valid=True
if(name.count(' ')>0):
    if (name[0]==' ' or name[len(name)-1]==' ')  :
        valid=False
    else:
        valid=True
else:
    valid=False
if (age<18 or age>60):
    valid=False
if (mobile.isdigit()==False or len(mobile)!=10 or mobile[0]=='0') :
    valid=False
if (mail.count('@')==0 or mail.count('.')==0 or mail[0].isalpha()==False) :
    valid=False
if valid:
    print("User Profile is VALID")
else:
    print("User Profile is INVALID")

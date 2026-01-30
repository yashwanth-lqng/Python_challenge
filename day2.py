id=input("Enter your ID: ")
mail=input("Enter your Email: ")
password=input("Enter your Password: ")
refcode=input("Enter your Referral Code: ")
is_approved=True

if id[0]!='C' or id[1]!='S' or id[2]!='E' or id[3]!='-' or len(id)!=7 or id[4].isdigit()==False or id[5].isdigit()==False or id[6].isdigit()==False:
    is_approved=False

has_different_symbol=('!' in mail) or ('#' in mail) or ('$' in mail) or ('%' in mail) or ('&' in mail) or ('*' in mail) or ('(' in mail) or (')' in mail) or ('-' in mail) or ('_' in mail) or ('=' in mail) or ('+' in mail)

if mail.count('@')!=1 or mail.count('.')!=1 or mail[0].isalpha()==False or mail[-1].isalpha()==False or mail[-4]!='.' or mail[-3]!='e' or mail[-2]!='d' or mail[-1]!='u' or has_different_symbol==True:
    is_approved=False

has_number=('0' in password) or ('1' in password) or ('2' in password) or ('3' in password) or ('4' in password) or ('5' in password) or ('6' in password) or ('7' in password) or ('8' in password) or ('9' in password)

if len(password)<8 or password[0].upper()!=password[0] or has_number==False:
    is_approved=False

if refcode[0]!='R' or refcode[1]!='E' or refcode[2]!='F' or len(refcode)!=6 or refcode[3].isdigit()==False or refcode[4].isdigit()==False or refcode[5]!='@':
    is_approved=False

if is_approved:
    print("APPROVED")
else:
    print("REJECTED")
def contains(email,special_char):
    for i in range(len(email)):
        if email[i]==special_char:
            return True
        
def email_validate(email):
    if len(email)>10 and email.islower() and (email[0]!='@' or '.') and (email[-1]!='@' or '.') and contains(email,'@') and contains(email,'.') and type(email)==str:
        print("Valid Email")
    else:
        print("Invalid Email")
email_validate("muthu@gmail.com")
email_validate("1000000@123.123")
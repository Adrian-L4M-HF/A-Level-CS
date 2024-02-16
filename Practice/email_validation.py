"""Email validation"""
"""         
The email should contain one and only one “@” sign

The email should contain at least one “.” sign located after
 the “@” sign. However it may contains more than one “.” sign
 for emails ending in .co.uk for instance
 
The email cannot contain any space or “#” signs

The “@” sign cannot be in the first position and
 there should be at least 1 character between the “@” and the “.” sign.
 
The email cannot end with a “.” sign
"""
def email_validation(Email):
    atSignPosition = -1
    number_of_atSign = 0
    if Email[-1] == ".":
       return "This is NOT a valid e-mail address"
    for i in range(0,len(Email)):
        if Email[i] == " " or Email[i] == "#":
            return "This is NOT a valid e-mail address"
        if Email[i] == "@":
            atSignPosition = i
            number_of_atSign += 1
            if Email[i+1] == ".":
               return "This is NOT a valid e-mail address"
            if "." not in Email[i:]:
                return "This is NOT a valid e-mail address"           
    if atSignPosition < 1 or number_of_atSign > 1:
        return "This is NOT a valid e-mail address"
    return "This seems to be a valid e-mail address"
    

print(email_validation("gfc.bvb@gvcb.org.uk"))
print(email_validation("a@.com"))
print(email_validation("a @.com"))
print(email_validation("a@.c##om"))
print(email_validation("a@.com."))
print(email_validation("a@.c@l.om"))
print(email_validation("@hghnb.colm"))


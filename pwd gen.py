import string
import random
import secrets
n=int(input("enter the length of password but it should not be more than 10 figures"))
print("the password will consist of letter and digits only")
d=string.digits
l=string.ascii_letters
fig=l+d
result=''
for i in range(n):
    result+=''.join(secrets.choice(fig))
print("the required password is=",result)

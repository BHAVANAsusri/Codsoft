import string
import random 

def strong_password(length=10):
    password=string.ascii_letters+string.digits+string.punctuation
    suggest=' '.join(random.choice(password) for i in range (length))
    print("Password : ",suggest)

strong_password()

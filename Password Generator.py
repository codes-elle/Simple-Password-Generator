import random #ability to create a random ouput
import string #give more complexity

def generate_pw(length: int = 10): #generated password length is int variable
    #create a list and store the ascii letters, digits, and punctuations in the alphabet variable
    alphabet = string.ascii_letters + string.digits + string.punctuation  
    #randomize alphabet variable, and however long the length is set.  
    password = "".join(random.choice(alphabet) for i in range(length)) 
    return password #

password = generate_pw()
print(f"Generated password: {password}")

import re

def check(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if(re.fullmatch(regex, email)):
        return True
 
    else:
        return False

def register(email, password):
    content = False
    with open('bdd.txt', 'r') as f:
        lines = f.readlines()
        for ji in lines:
            if ji.split(';')[0] == email:
                content = True
    isOk = False
    with open('bdd.txt', 'a') as f:
        if (check(email) and len(password) >= 6 and content == False):
            f.write(f'{email};{password}\n')
            isOk=True
    return isOk
            
def login(email, password):
    isOk = False
    with open('bdd.txt', 'r') as f:
        lines = f.readlines()
        for ji in lines:
            if ji.split(';')[0] == email and ji.split(';')[1] == password+'\n':
                isOk = True
    return isOk

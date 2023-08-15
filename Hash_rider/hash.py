import hashlib

email= 'shahalam@gmail.com'
pwd='ChairOnTheTableWith3Legs'
pwd_encode=pwd.encode()
pwd_hash=hashlib.md5(pwd_encode).hexdigest()

your_email= 'shahalam@gmail.com'
your_pwd='ChairOnTheTableWith3Legs'
hashed_your_pwd=hashlib.md5(your_pwd.encode()).hexdigest()
if your_email==email and hashed_your_pwd==pwd_hash:
    print('Right user')
else:
    print('worng password')

hacker_email='shahalam@gmail.com'
hacker_pwd='ae3c2a537c856b96d546c3688b4fe902'

print(pwd)
print(pwd_hash)



def make_upper(s):
    upper_string=s.upper()
    print(upper_string)
    
def make_capital(s):
    str3=' '.join(i.capitalize()  for i in s.split(' '))
    print(str3)


def make_lower(s):
    lower_string=s.lower()
    print(lower_string)
    

s='mAke tHe sTriNg'
make_upper(s)
make_capital(s)
make_lower(s)

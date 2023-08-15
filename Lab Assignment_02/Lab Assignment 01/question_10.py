

def create_new_string(s,a):
    with open('file.txt','a') as file:
        Flage=False
        for word in s.split():
            if word in a:
                print(word, end=' ')
                Flage=True
                continue
            if Flage==True:
                file.write(word+' ')
                Flage=False
        
a = ['Oh', 'Emelia', 'to']
s = "Oh I got two tickets for Dhaka. I and Emelia love visit different places very much. This time we are going to Bangladesh."
create_new_string(s,a)


# with open('message.txt','a') as filewrite:
#     filewrite.write('I love to play football\n')

with open('message.txt','r') as fileread:
    text=fileread.read()
    print(text)
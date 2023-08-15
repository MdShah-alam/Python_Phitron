
with open('file.txt','r') as file:
    lines=file.read()
    sentence=lines.center(len(lines)+20,'*')
    print(sentence)

Find = True
with open('books.txt','r') as file:
    while Find:
        lines=file.read()
        for word in lines.split():
            if word!='--':
                print(word,end=' ')
            else:
                break
        k=input('\nEnter - to continue ,Enter q to que : ')
        if k=='q':
            Find = False
               
file.close()

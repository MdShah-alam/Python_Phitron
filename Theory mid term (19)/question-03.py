
def nearly_equal( a , b):
    alen=len(a)
    blen=len(b)
    
    for i in range(0, alen,1):
        Flage=True
        for j in range(0,blen , 1):
            if a[i]==b[j]:
                Flage=False
                continue
        if Flage:
            print('False')
            return
    print('True')


a=input('Enter a string :')
b=input('Enter b string :')
nearly_equal(a,b)

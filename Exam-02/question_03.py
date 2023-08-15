
s = 'Programming Hero is the best'

for word in s.split(' '):
    st=''
    for i in range(len(word)-1,-1,-1):
        st+=word[i]
    print(st , end=' ')
    

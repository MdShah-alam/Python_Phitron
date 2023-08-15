word=input('Enter the input : ')
print("The input is ",word)
size=len(word)
for i in range(0,size,2):
    print("index [", i ,"] " , word[i])
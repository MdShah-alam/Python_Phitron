
# Input : x3b4U5i2
# Output : bbbbiiUUUUUxxx

Input='x3b4U5i2'
Output=''

for i in range(2,len(Input),4):
    letter=Input[i]
    number=int(Input[i+1])
    for k in range(0,number,1):
        Output+=letter
        
for st in range(len(Input)-3,-1,-4):
    number=int(Input[st])
    letter=Input[st-1]
    for i in range(0,number,1):
        Output+=letter

print(Output)
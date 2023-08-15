# word=input('Enter a word : ')
# print('The word is : ',word)
# # Remeve frist n character form a string
# new_word=word[2:]
# print('After removing : ',new_word)
# # close the 1st exercise

# n=int(input('Enter the size of array : '))
# for i in range(0,n,1):
#     array[i]=int(input())

# if array[0]==array[n-1]:
#     print('True')
# else:
#     print('False')

def first_last_same(numberList):
    print("Given list:", numberList)
    
    first_num = numberList[0]
    last_num = numberList[-1]
    
    if first_num == last_num:
        return True
    else:
        return False

numbers_x = [10, 20, 30, 40, 10]
print("result is", first_last_same(numbers_x))

numbers_y = [75, 65, 35, 75, 30]
print("result is", first_last_same(numbers_y))
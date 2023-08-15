
def palindrome (word):
    lenght=len(word)
    reverse_word=''
    for i in range(lenght-1 ,-1,-1):
        reverse_word+=word[i]

    print(reverse_word==word)
    
word = input('Enter a word :')
palindrome(word)
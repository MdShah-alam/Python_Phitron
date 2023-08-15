
def replace_word(s,rplc):
    lst=s.split(' ')
    for word in lst:
        for i , rp in enumerate(rplc):
            if word==rp:
                s=s.replace(word,rplc[i+1])
    return s
   
replace_with = ["chief", "thief", "superintendent", "sweeper", "married", "left", "tried", "died"]
s = "I am the chief of Baghdad. Before that I used to be a superintendent of Bank Asia. Things have changed a lot since Jorina married me. A lot of girls tried to marry me."
print(replace_word(s,replace_with))

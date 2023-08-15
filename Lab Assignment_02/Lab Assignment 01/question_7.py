def replace_comma_with_space(text):
    st=""
    for word in text:
        if word==',':
            st+=" "
        else:
            st+=word
    return st
    
    
s = "I,have,been,practising,python,since,the,course,started"

output = replace_comma_with_space(s)
print(output)

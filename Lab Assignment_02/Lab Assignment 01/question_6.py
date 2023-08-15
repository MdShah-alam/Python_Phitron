def clean_string(text):
    output=""
    for s in text:
        if (s>='A' and s<='Z') or (s>='a' and s<='z'):
            output+=s
    print(output)
    return output
    
s = "P::::::,,,,,h;;;;i,,,t--r;,:o..N"

output = clean_string(s)
print(output)
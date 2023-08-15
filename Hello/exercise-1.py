current_value=0
previous_value=0

sum=0
for num in range(1 ,10,1) :
    sum=current_value+previous_value
    about_me=f'Current value {current_value} previous value {previous_value}  sum  {sum}'
    print(about_me)
    previous_value=current_value
    current_value=num

def func(arg1, arg2, arg3=4, arg4=5):
    print(arg1, arg2, arg3, arg4)

func(6, 7)  # 6 7 4 5
func(4, 5, arg3=6)  # 4 5 6 5
# func() missing 2 required positional arguments :'arg1' and 'arg2'
# func(3, 4, arg2=1) multiple value for argument 'arg2'
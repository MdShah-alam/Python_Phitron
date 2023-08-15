
def getResult(A, B):

    Sum = A ^ B

    Carry = A & B

    print("Sum ", Sum)
    print("Carry", Carry)

A =int(input())
B =int(input())

getResult(A, B)

def primenumber(n):

    if n < 0:
        return ("negative num not allowed")
    elif n == 1:
        return ("input needed should be greater than 1")
    elif  not isinstance (n, int):
        return ("strings not allowed input an integer")
    elif n == 0:
        return ("should not be 0")


    for number in range(2,n+1):

       if all(number%i!=0 for i in range(2,number)):
            print (number)

primenumber(4)


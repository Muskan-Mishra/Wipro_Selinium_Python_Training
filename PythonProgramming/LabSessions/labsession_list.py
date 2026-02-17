from email.quoprimime import body_decode


def largest_num(a):
    return max(a)


a =[2,5,8,9,10]
print(largest_num(a))




def remove_even(a):
    if a%2 != 0:
        return 1
    else:
        return 0

a =[2,5,8,9,10]
print(remove_even(9))







def mult(a):
    p = 1
    for i in a:
        p *= i
    return p
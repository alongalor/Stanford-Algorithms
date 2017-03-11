def karatsuba(x,y):
    if get_len(x)==1:
        return x*y
    else:
        return 10**get_len(x)*karatsuba(get_a(x),get_a(y)) + 10**(get_len(x)//2)*(karatsuba(
            get_a(x),get_b(y)) + karatsuba(get_b(x),get_a(y))) + karatsuba(get_b(x),get_b(y))

def get_len(n):
    return len(str(n))
    
def get_a(n):
    return n//10**(get_len(n)//2)

def get_b(n):
    return n%10**(get_len(n)//2)